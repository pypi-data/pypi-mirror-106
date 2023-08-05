# ml

# https://towardsdatascience.com/logistic-regression-model-tuning-with-scikit-learn-part-1-425142e01af5
# https://www.kaggle.com/anshigupta01/titanic-prediction-top-17
# https://towardsdatascience.com/building-a-logistic-regression-in-python-step-by-step-becd4d56c9c8

import sklearn.svm as __svm

class __result :
    model = None
    accuracy = None
    y_pred = None

def run (a_x_train,a_x_test,a_y_train,a_y_test) :
    loc_model = __svm.SVC()
    loc_model.fit(a_x_train,a_y_train)
    loc_y_pred = loc_model.predict(a_x_test)
    loc_accuracy = loc_model.score(a_x_test,a_y_test)
    loc_result = __result()
    loc_result.model = loc_model
    loc_result.accuracy = loc_accuracy
    loc_result.y_pred = loc_y_pred
    return loc_result
    