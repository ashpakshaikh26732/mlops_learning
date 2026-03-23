import hydra
from omegaconf import DictConfig, OmegaConf 
import logging 

@hydra.main(version_base=None, config_path='./configs' , config_name='main')
def main(cfg : DictConfig)->None  : 
    cfg = OmegaConf.to_yaml(cfg)
    print(cfg)    
    
    
    
if __name__ == '__main__' : 
    main()

