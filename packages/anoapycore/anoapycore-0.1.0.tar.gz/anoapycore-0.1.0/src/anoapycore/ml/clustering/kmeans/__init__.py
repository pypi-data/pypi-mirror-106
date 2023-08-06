# ml

import numpy as __np
from sklearn.cluster import KMeans as __model
from kneed import KneeLocator as __find_k
import matplotlib.pyplot as __plt

class __result :
    centroids = None # cluster centers
    elbow_chart = None
    label = [] # filtered label of clusters
    labels = None # predict the labels of clusters
    labels_unique = None # predict the labels unique of clusters
    optimum_k = None
    sse = None # sum of the squared errors

def run (a_data,a_features,a_max_clusters_to_try=11) :
    # find optimum k
    loc_sse = []
    for k in range(1,a_max_clusters_to_try):
        loc_model = __model(n_clusters=k)
        loc_model.fit(a_data[a_features])
        loc_sse.append(loc_model.inertia_)
    loc_find_k = __find_k(range(1,a_max_clusters_to_try),loc_sse,curve="convex",direction="decreasing")
    loc_optimum_k = loc_find_k.elbow
    # run model with optimum k
    loc_model = __model(n_clusters=loc_optimum_k)
    loc_model.fit(a_data[a_features])
    # predict the labels of clusters.
    loc_label = []
    label = loc_model.fit_predict(a_data[a_features])
    loc_unique_labels = __np.unique(label)
    loc_new_data = a_data[a_features]
    for i in loc_unique_labels :
        # loc_label[i] = loc_new_data[label == i]
        loc_label.insert(i,loc_new_data[label == i])
    loc_elbow_chart = __elbow_chart(a_max_clusters_to_try,loc_sse)
    # get result
    loc_result = __result()
    loc_result.centroids = loc_model.cluster_centers_
    loc_result.elbow_chart = loc_elbow_chart 
    loc_result.label = loc_label
    loc_result.labels = label
    loc_result.labels_unique = loc_unique_labels
    loc_result.optimum_k = loc_optimum_k
    loc_result.sse = loc_sse
    # final
    return loc_result
    
def __elbow_chart (a_max_clusters_to_try,a_sse) :
    loc_plot = __plt.figure()
    __plt.style.use("fivethirtyeight")
    __plt.plot(range(1,a_max_clusters_to_try),a_sse)
    __plt.xticks(range(1,a_max_clusters_to_try))
    __plt.xlabel("Number of Clusters")
    __plt.ylabel("SSE")
    __plt.close()
    return loc_plot
    
def plot (a_model,a_column_x,a_column_y) :    
    __plt.xlabel(a_column_x)
    __plt.ylabel(a_column_y)
    for i in a_model.labels_unique :
        __plt.scatter(a_model.label[i][:][a_column_x],a_model.label[i][:][a_column_y],label=i)
    __plt.legend()
    __plt.show()    
