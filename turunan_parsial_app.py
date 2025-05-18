import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Judul aplikasi
st.title("Aplikasi Turunan Parsial dan Grafik 3D")
st.write("Masukkan fungsi dua variabel f(x, y) dan titik evaluasi (x₀, y₀)")

# Input dari pengguna
fungsi_input = st.text_input("Fungsi f(x, y)", "x*2 + y*2")
x0 = st.number_input("x₀", value=1.0)
y0 = st.number_input("y₀", value=1.0)

# Definisi simbol
x, y = sp.symbols('x y')

try:
    # Konversi fungsi
    f_xy = sp.sympify(fungsi_input)

 # Turunan parsial
    df_dx = sp.diff(f_xy, x)
    df_dy = sp.diff(f_xy, y)

    # Evaluasi fungsi dan turunannya di titik (x0, y0)
    f_val = f_xy.evalf(subs={x: x0, y: y0})
    df_dx_val = df_dx.evalf(subs={x: x0, y: y0})
    df_dy_val = df_dy.evalf(subs={x: x0, y: y0})

    # Tampilkan hasil
    st.latex(f"f(x, y) = {sp.latex(f_xy)}")
    st.write("Nilai fungsi di titik (x₀, y₀):", f_val)  # ← Baris tambahan sesuai permintaan
    st.latex(f"\\frac{{\\partial f}}{{\\partial x}} = {sp.latex(df_dx)}, \\quad f_x({x0}, {y0}) = {df_dx_val}")
    st.latex(f"\\frac{{\\partial f}}{{\\partial y}} = {sp.latex(df_dy)}, \\quad f_y({x0}, {y0}) = {df_dy_val}")

    # Plot permukaan dan bidang singgung
    st.subheader("📈 Grafik Permukaan & Bidang Singgung")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X_vals = np.linspace(x0 - 2, x0 + 2, 50)
    Y_vals = np.linspace(y0 - 2, y0 + 2, 50)
    X, Y = np.meshgrid(X_vals, Y_vals)

 f_lambdified = sp.lambdify((x, y), f_xy, 'numpy')
    Z = f_lambdified(X, Y)

    # Hitung bidang singgung
    Z_tangent = float(f_val) + float(df_dx_val) * (X - x0) + float(df_dy_val) * (Y - y0)

    # Gambar grafik
    ax.plot_surface(X, Y, Z, alpha=0.7, cmap='viridis')
    ax.plot_surface(X, Y, Z_tangent, alpha=0.5, color='red')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    ax.set_title('Permukaan dan Bidang Singgung')
    st.pyplot(fig)

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
