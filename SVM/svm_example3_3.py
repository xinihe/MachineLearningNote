# _*_coding:utf-8_*_
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC, SVC

X, y = make_moons(n_samples=100, noise=0.15, random_state=42)

def plot_dataset(X, y, axes):
    plt.plot(X[:, 0][y == 0], X[:, 1][y == 0], 'bs')
    plt.plot(X[:, 0][y == 1], X[:, 1][y == 1], 'g*')
    plt.axis(axes)
    plt.grid(True, which='both')
    plt.xlabel(r'$x_1$', fontsize=20)
    plt.ylabel(r'$x_2$', fontsize=20, rotation=0)

# 展示图像
def plot_predictions(clf, axes):
    x0s = np.linspace(axes[0], axes[1], 100)
    x1s = np.linspace(axes[2], axes[3], 100)
    x0, x1 = np.meshgrid(x0s, x1s)
    X = np.c_[x0.ravel(), x1.ravel()]
    y_pred = clf.predict(X).reshape(x0.shape)
    # 下面填充一个等高线, alpha表示透明度
    plt.contourf(x0, x1, y_pred, cmap=plt.cm.brg, alpha=0.2)


Poly_kernel_svm_clf = Pipeline((('scaler', StandardScaler()),
                                ('svm_clf', SVC(kernel='poly', degree=3, coef0=1, C=5))
                                ))
Poly_kernel_svm_clf.fit(X, y)
# 下面做一个对比试验，看看degree的值的变换
Poly_kernel_svm_clf_plus = Pipeline((('scaler', StandardScaler()),
                                     ('svm_clf', SVC(kernel='poly', degree=10, coef0=1, C=5))
                                     ))
Poly_kernel_svm_clf_plus.fit(X, y)

plt.subplot(121)
plot_predictions(Poly_kernel_svm_clf, [-1.5, 2.5, -1, 1.5])
plot_dataset(X, y, [-1.5, 2.5, -1, 1.5])
plt.title(r'$d=3, r=1, C=5$', fontsize=18)

plt.subplot(122)
plot_predictions(Poly_kernel_svm_clf_plus, [-1.5, 2.5, -1, 1.5])
plot_dataset(X, y, [-1.5, 2.5, -1, 1.5])
plt.title(r'$d=10, r=100, C=5$', fontsize=18)
plt.show()
