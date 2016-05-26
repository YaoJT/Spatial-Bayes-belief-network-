##Class definition: 
class Bayes_s():
    def __init__(self,classfication_raster,factor_list):
        cla_raster = classfication_raster
        factor_lst = factor_list
## bayes_net is a list representing the bayes net and break value of every factor
        bayes_net = []
    def update_net(self,update_classfication_raster,update_factor_list):
## update network with the training data        
    def predict(self,factor_list):
## create classfication raster with the factor rasters and updated network
