from ..utils import LOG
from .base import DeepvacCast, FXQuantizeAndScript

class ScriptCast(DeepvacCast):
    def __init__(self, deepvac_core_config):
        super(ScriptCast,self).__init__(deepvac_core_config)

    def auditConfig(self):
        if not self.config.script_model_dir:
            return False

        if not self.config.static_quantize_dir:
            return True
            
        if self.core_config.is_forward_only and self.core_config.test_loader is None:
            LOG.logE("You must set config.core.test_loader in config.py when config.core.static_quantize_dir is enabled.", exit=True)
        if not self.core_config.is_forward_only and self.core_config.val_loader is None:
            LOG.logE("You must set config.core.val_loader in config.py when config.core.static_quantize_dir is enabled.", exit=True)

        return True

    def process(self, cast_output_file=None):
        output_script_file = self.config.script_model_dir
        if cast_output_file:
            output_script_file = '{}/script__{}.pt'.format(self.core_config.output_dir, cast_output_file)

        LOG.logI("config.script_model_dir found, save script model to {}...".format(output_script_file))

        script_model = FXQuantizeAndScript(self.core_config, output_script_file)
        script_model.save()

        if self.config.dynamic_quantize_dir:
            LOG.logI("You have enabled config.dynamic_quantize_dir, will dynamic quantize the model...")
            script_model.saveDQ()

        if self.config.static_quantize_dir:
            LOG.logI("You have enabled config.static_quantize_dir, will static quantize the model...")
            script_model.saveSQ()
