import numpy as np
from scipy.special import logsumexp
from sklearn.utils import check_random_state

from . import hsmm_base, hsmm_utils
from .hsmm_base import HSMM
from .hsmm_utils import log_mask_zero

# Explicit Duration HSMM with Multinomial (Discrete) Emissions
class MultinomialHSMM(HSMM):
    def __init__(self, n_states=2, n_durations=5, n_iter=20, tol=1e-2, rnd_state=None):
        super().__init__(n_states, n_durations, n_iter, tol, rnd_state)

    def _init(self, X):
        super()._init()
        # note for programmers: for every attribute that needs X in score()/predict()/fit(),
        # there must be a condition 'if X is None' because sample() doesn't need an X, but
        # default attribute values must be initiated for sample() to proceed.
        if True:   # always change self.n_symbols
            if X is None:   # default for sample()
                self.n_symbols = 2
            else:
                self.n_symbols = np.max(X) + 1
        if not hasattr(self, "emit"):
            # like in hmmlearn, whether with X or not, default self.emit would be random
            rnd_checked = check_random_state(self.rnd_state)
            init_emit = rnd_checked.rand(self.n_states, self.n_symbols)
            # normalize probabilities, and make sure we don't divide by zero
            init_sum = init_emit.sum(1)
            zero_sums = (init_sum == 0)   # which rows are all zeros?
            init_emit[zero_sums] = 1   # set all rows with all zeros to all ones
            init_sum[zero_sums] = self.n_symbols
            self.emit = init_emit / init_sum[None].T

    def _check(self):
        super()._check()
        # emission probabilities
        self.emit = np.asarray(self.emit)
        if self.emit.shape != (self.n_states, self.n_symbols):
            raise ValueError("emission probabilities (self.emit) must have shape ({}, {})"
                             .format(self.n_states, self.n_symbols))
        if not np.allclose(self.emit.sum(axis=1), 1.0):
            raise ValueError("emission probabilities (self.emit) must add up to 1.0")

    def _dur_init(self):
        # non-parametric duration
        if not hasattr(self, "dur"):
            self.dur = np.full((self.n_states, self.n_durations), 1.0 / self.n_durations)

    def _dur_check(self):
        self.dur = np.asarray(self.dur)
        if self.dur.shape != (self.n_states, self.n_durations):
            raise ValueError("duration probabilities (self.dur) must have shape ({}, {})"
                             .format(self.n_states, self.n_durations))
        if not np.allclose(self.dur.sum(axis=1), 1.0):
            raise ValueError("duration probabilities (self.dur) must add up to 1.0")

    def _dur_probmat(self):
        # non-parametric duration
        return self.dur

    def _dur_mstep(self, new_dur):
        # non-parametric duration
        self.dur = new_dur
        
    def _emission_logprob(self, X):
        return log_mask_zero(self.emit[:, np.concatenate(X)].T)
    
    def _emission_pre_mstep(self, gamma, emission_var):
        # note for programmers: refer to "emission_var" as emission_var[0] here. Maybe this
        # is unidiomatic, but this is done to force pass-by-reference to the np.ndarray.
        # note #2: The "emssion_var" here is the cumulative concatenation of the gammas of each
        # observation sequence, so most likely you wouldn't modify this for your own subclass.
        if emission_var[0] is None:   # initial
            emission_var[0] = gamma
        else:
            old_emitlength = emission_var[0].shape[0]
            emission_var[0].resize(old_emitlength + gamma.shape[0], self.n_states)
            emission_var[0][old_emitlength:] = gamma

    def _emission_mstep(self, X, emission_var):
        # note for programmers: now refer to "emission_var" as it is, here.
        denominator = logsumexp(emission_var, axis=0)
        weight_normalized = np.exp(emission_var - denominator)
        iverson = (X.T == np.arange(self.n_symbols)[:,None])   # iverson bracket
        self.emit = (weight_normalized[:,:,None] * iverson[:,None].T).sum(0)
 
    def _state_sample(self, state, rnd_state=None):
        emit_cdf = np.cumsum(self.emit[state, :])
        rnd_checked = check_random_state(rnd_state)
        return [(emit_cdf > rnd_checked.rand()).argmax()]   # shape of X must be (n_samples, 1)