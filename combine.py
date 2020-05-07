import numpy as np
import omegaconf
from omegaconf import OmegaConf

"""A simple example for using guild config dependency with OmegaConf"""
def main():
   
   hparams = OmegaConf.load('./config1.yml')
   trainer_config = OmegaConf.load('./config2.yml')
   conf = OmegaConf.merge(hparams, trainer_config)

   # Print or save the merged run configuration
   print(conf.pretty())

   # Here is an example of why I need to decouple my config params into different yml files
   #  module = MyLightningModule(hparams)
   #  trainer = Trainer(**trainer_config)

   result = conf.a + conf.b + conf.x + conf.y
   return result

if __name__ == "__main__":
   y = main()
   print("combined value: %f" % y)

