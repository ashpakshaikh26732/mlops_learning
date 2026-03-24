import hydra
from omegaconf import DictConfig, OmegaConf 
import logging 
import os 
import dataclasses 





# @hydra.main(version_base=None, config_path='./configs' , config_name='main')
# def main(cfg : DictConfig)->None  : 
    
#     print(cfg)

#     # convert cfg which is dict to yaml like file or output 
#     # code 
#     cfg = OmegaConf.to_yaml(cfg)
#     print(cfg)    
    
#     # multirun 
#     # python main.py hydra.mode=multirun db=mysql,postgresql schema=warehouse,support,school 
#     # it is going to lauch 6 jobs for each permitution 
    
    
#     # working directry 
#     # by default hydra creates new output dir 
#     print(f"Working directory : {os.getcwd()}")
#     print(f"Output directory  : {hydra.core.hydra_config.HydraConfig.get().runtime.output_dir}")
    
#     # same working dir and output dir 
#     # for this need to overide hydra.job.chdir=True  
#     # command python main.py hydra.job.chdir=True  by default it is false 

#     return 
    
    
# logging with hydra 
# log = logging.getLogger(__name__)
# @hydra.main(version_base=None , config_path='./configs',config_name='main') 
# def main(_cfg : DictConfig)->None  : 
        
#     log.info("info logging")
#     log.debug("debugging")    
        
#     NotImplemented
    
    
# debugging
# print config without running function by adding --cfg or -c to command like it take 1 argumet which config 
# to print job , hydra  , all , by using --pakage can output subset of config   

# tab completion need to install bash for project once we do this we can get completion by using tab 
# log = logging.getLogger(__name__)
# @hydra.main(version_base=None , config_path='./configs' , config_name='main')
# def main(cfg :DictConfig): 
#     print(cfg)


# structured config tut 


def main() : 
    NotImplemented

if __name__ == '__main__' : 
    main()

