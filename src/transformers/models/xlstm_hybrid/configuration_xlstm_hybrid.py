


from ...configuration_utils import PretrainedConfig


class _XlstmHybridConfig(PretrainedConfig):

    model_type = "xlstm_hybrid"

    def __init__(
        self,
        window_size: int = 256,
        num_sink_tokens: int = 4,
        i_gate_init_b: int = -10,
        f_gate_init_b: int = 10,
        o_gate_init_b: int = 0,
        **kwargs,
    ):
        self.window_size = window_size
        self.num_sink_tokens = num_sink_tokens
        self.i_gate_init_b = i_gate_init_b
        self.f_gate_init_b = f_gate_init_b
        self.o_gate_init_b = o_gate_init_b
        super().__init__(**kwargs)