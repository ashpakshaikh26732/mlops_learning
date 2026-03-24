# # from dataclasses import dataclass
# # import hydra 
# # from omegaconf import OmegaConf , DictConfig 
# # from hydra.core.config_store import ConfigStore

# # cs = ConfigStore.instance()

# # @dataclass 
# # class db: 
# #     port : int 
# #     link : str 

# # cs.store(name='config' , node=db)


# # @hydra.main(version_base=None , config_path='./configs' , config_name='main') 
# # def main(cfg : db):
# #     print(type(cfg)) 
# #     # cfg = OmegaConf.to_yaml(cfg)
# #     # print(cfg) 
    
    
    

    
# # if __name__ == "__main__" : 
    
# #     main() 
    
    




# from dataclasses import dataclass
# from typing import List
# import hydra 
# from omegaconf import DictConfig , OmegaConf 
# from hydra.core.config_store import ConfigStore
# from hydra.core.hydra_config import HydraConfig

# @dataclass
# class Model:
#     name: str

# @dataclass
# class Data:
#     modality: str
#     CT_clip_value_min: int
#     CT_clip_value_max: int
#     val_count: int
#     train_count: int
#     num_classes: int
#     batch: int
#     num_replicas: int

#     image_shape: List[int]
#     label_shape: List[int]
#     image_patch_shape: List[int]
#     label_patch_shape: List[int]

#     stage_patches_per_volume: int
#     stage1_fg_ratio: float
#     stage2_fg_ratio: float
#     stage3_fg_ratio: float
#     stage3_hard_sample_ratio: float

#     stage2_intra_class_ratio: List[float]

#     vis: bool
#     aws: bool
#     image_patch: bool

#     target_spacing: List[float]

#     num_patches: int
#     dataset_url: str
#     tarfile_name: str

#     class_names: List[str]
#     class_weights: List[float]
#     output_weights: List[float]
#     loss_weights: List[float]

# @dataclass
# class Checkpoint:
#     local_checkpoint_dir: str
#     hf_repo_id: str
#     hf_path_in_repo: str
#     artifact_name: str

#     total_step: int
#     warmup_step: int
#     target_lr: float
#     min_delta: float
#     patiance: int

#     batches_per_epoch: int
#     total_epoch: int
#     log_dir: str

#     stage_2_epoch: int
#     stage_3_epoch: int
#     ohem_call_duration: int
#     duration_to_save_checkpoints: int

#     checkpoint_path: str

# @dataclass
# class Optimizer:
#     starting_lr: float
#     weight_decay: float

# @dataclass
# class Task01UnetPP:
#     task: int
#     model: Model
#     data: Data
#     checkpoint: Checkpoint
#     optimizer: Optimizer
#     loss: str
    
# cs = ConfigStore.instance() 
# cs.store(name='task_01' , node=Task01UnetPP) 

# @hydra.main(config_path='./configs',config_name='main' , version_base=None) 
# def main(cfg :Task01UnetPP) -> None:
    
#     # accessing undefind value 
#     ufm = cfg.ufm
#     assert ufm == 'main'
    
#     cfg = OmegaConf.to_yaml(cfg)
#     print(cfg)

#     print(HydraConfig.get().job.name)
    



    
# if __name__ == "__main__" : 
#     main() 




from dataclasses import dataclass 
import hydra 
from omegaconf import DictConfig , OmegaConf 





def main() : 
    NotImplemented

if __name__ == "__main__": 
    
    main() 