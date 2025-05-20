import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#мои данные
x = np.array([2, 4, 6, 8, 10, 12])
y = np.array([1.08, 0.36, 0.21, 0.12, 0.09, 0.04])
#функции
def lin(x, a, b): return a * x + b
def power(x, a, b): return b * x**a
def expo(x, a, b): return b * np.exp(a * x)
def quad(x, a, b, c): return a * x**2 + b * x + c

#нахождение коэффициентов
coef_lin, fallibility = curve_fit(lin, x, y)
coef_pow, fallibility = curve_fit(power, x, y, p0=[1, -1]) #доп праметр тк функция нелинейная, не знаем откуда начать подбор параметров. 1 тк y положительные, а -1 тк y убывают
coef_exp, fallibility = curve_fit(expo, x, y, p0=[1, -0.5])
coef_quad, fallibility = curve_fit(quad, x, y)

#для вычисления ошибки
def error(real, predicted): 
  return np.sum((real - predicted)**2)

#построение аппроксимаций
y_fit_lin = lin(x, *coef_lin)
y_fit_pow = power(x, *coef_pow)
y_fit_exp = expo(x, *coef_exp)
y_fit_quad = quad(x, *coef_quad)
#нахождение ошибок
err_lin = error(y, y_fit_lin)
err_pow = error(y, y_fit_pow)
err_exp = error(y, y_fit_exp)
err_quad = error(y, y_fit_quad)

#графики
x_plot = np.linspace(x.min(), x.max(), 200)
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

axs[0, 0].plot(x_plot, lin(x_plot, *coef_lin), 'r', label=f'ошибка: {err_lin:.4f}')
axs[0, 0].scatter(x, y)
axs[0, 0].set_title("линейная модель")
axs[0, 0].legend()
axs[0, 0].grid()

axs[0, 1].plot(x_plot, power(x_plot, *coef_pow), 'g', label=f'ошибка: {err_pow:.4f}')
axs[0, 1].scatter(x, y)
axs[0, 1].set_title("степенная модель")
axs[0, 1].legend()
axs[0, 1].grid()

axs[1, 0].plot(x_plot, expo(x_plot, *coef_exp), 'b', label=f'ошибка: {err_exp:.4f}')
axs[1, 0].scatter(x, y)
axs[1, 0].set_title("показательная модель")
axs[1, 0].legend()
axs[1, 0].grid()

axs[1, 1].plot(x_plot, quad(x_plot, *coef_quad), 'purple', label=f'ошибка: {err_quad:.4f}')
axs[1, 1].scatter(x, y)
axs[1, 1].set_title("квадратичная модель")
axs[1, 1].legend()
axs[1, 1].grid()

plt.tight_layout()
plt.show()

#общий график
plt.figure(figsize=(10, 6))
plt.plot(x_plot, lin(x_plot, *coef_lin), 'r', label='линейная')
plt.plot(x_plot, power(x_plot, *coef_pow), 'g', label='степенная')
plt.plot(x_plot, expo(x_plot, *coef_exp), 'b', label='показательная')
plt.plot(x_plot, quad(x_plot, *coef_quad), 'purple', label='квадратичная')
plt.scatter(x, y, color='black', label='данные')
plt.legend()
plt.title('сравнение моделей аппроксимации')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

#вывод
print("параметры моделей и ошибки:")
print(f"линейная: y = {coef_lin[0]:.4f}x + {coef_lin[1]:.4f}, S = {err_lin:.4f}")
print(f"степенная: y = {coef_pow[0]:.4f}x^{coef_pow[1]:.4f}, S = {err_pow:.4f}")
print(f"показательная: y = {coef_exp[0]:.4f}e^({coef_exp[1]:.4f}x), S = {err_exp:.4f}")
print(f"квадратичная: y = {coef_quad[0]:.4f}x² + {coef_quad[1]:.4f}x + {coef_quad[2]:.4f}, S = {err_quad:.4f}")

#лучшая модель
errors = {
    "линейная": err_lin,
    "степенная": err_pow,
    "показательная": err_exp,
    "квадратичная": err_quad
}
best = min(errors, key=errors.get)
print(f"\nнаилучшая аппроксимация: {best} модель (S = {errors[best]:.4f})")
