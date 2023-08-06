from parlai.core.agents import add_datapath_and_model_args, create_agent_from_opt_file
from parlai.core.build_data import modelzoo_path
from openchat.base import ConvAI2Agent, Seq2SeqLM


class BlenderGenerationAgent(ConvAI2Agent, Seq2SeqLM):

    def __init__(self, model: str, device: str, maxlen: int) -> None:
        model = self.check_agent(model)
        maxlen = maxlen if maxlen > 0 else self.default_maxlen()

        if "xxlarge" in model:
            size = "9B"
        elif "xlarge" in model:
            size = "3B"
        elif "large" in model:
            size = "1Bdistill"
        elif "medium" in model:
            size = "400Mdistill"
        elif "small" in model:
            size = "90M"
        else:
            raise Exception("wrong model")

        option = self.set_options(
            name=f"zoo:blender/blender_{size}/model",
            device=device,
        )

        super().__init__(
            name=model,
            suffix="\n",
            device=device,
            maxlen=maxlen,
            model=create_agent_from_opt_file(option),
        )

    @staticmethod
    def available_models():
        return [
            "blender.small",
            "blender.medium",
            "blender.large",
            "blender.xlarge",
            "blender.xxlarge",
        ]

    @staticmethod
    def default_maxlen():
        return 128

    def set_options(self, name, device):
        option = {}
        add_datapath_and_model_args(option)
        datapath = option.get("datapath")
        option['model_file'] = modelzoo_path(datapath, name)
        option["override"] = {
            "no_cuda": False if "cuda" in device else True,
        }

        if "cuda:" in device:
            option["override"]["gpu"] = int(device.split(":")[1])
        elif "cuda" in device:
            option["override"]["gpu"] = 0

        return option
