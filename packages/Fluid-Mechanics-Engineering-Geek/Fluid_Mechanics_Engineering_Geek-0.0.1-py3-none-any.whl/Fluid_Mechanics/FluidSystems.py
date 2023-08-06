from sympy import Symbol, diff, Expr, simplify, init_printing
from sympy.physics.vector import ReferenceFrame, curl
from matplotlib import pyplot as plt
import numpy as np
from typing import List


init_printing()


class System:
	def __init__(self):
		"""
		This class can do 6 things:
			calculate acceleration in each unit direction (2d and 3d)
			calculate shear strain rate (2d and 3d)
			volumetric strain equation
			calculate vorticity
			plot vector field and acceleration field
		"""
		self.t = Symbol("t")
		self.x = Symbol("x")
		self.y = Symbol("y")
		self.z = Symbol("z")

		self.u = Expr()
		self.v = Expr()
		self.w = Expr()

		print("Don't forget to set the u and v here manually only using passed variables!")

	def shear_strain_rate_equation(self):
		rate_e_xy = diff(self.u, self.y) + diff(self.v, self.x)
		rate_e_yz = diff(self.v, self.z) + diff(self.w, self.y)
		rate_e_xz = diff(self.u, self.z) + diff(self.w, self.x)
		return rate_e_xy, rate_e_yz, rate_e_xz

	def get_acceleration_equations(self):
		a_x = \
			diff(self.u, self.t) + \
			self.u * diff(self.u, self.x) + \
			self.v * diff(self.u, self.y) + \
			self.w * diff(self.u, self.z)
		a_y = \
			diff(self.u, self.t) + \
			self.u * diff(self.v, self.x) + \
			self.v * diff(self.v, self.y) + \
			self.w * diff(self.v, self.z)
		a_z = \
			diff(self.u, self.t) + \
			self.u * diff(self.w, self.x) + \
			self.v * diff(self.w, self.y) + \
			self.w * diff(self.w, self.z)

		return a_x, a_y, a_z

	def volumetric_strain_equation(self):
		print("Note: incompressible fluids have volumetric strain of 0, you can use this to get values")
		equation = diff(self.u, self.x) + diff(self.v, self.y)
		return equation

	def vorticity_equation(self):
		R = ReferenceFrame("R")
		i = R.x * self.u
		j = R.y * self.y
		k = R.z * self.w
		equation = (1 / 2) * curl(i + j + k, R)
		return equation

	def __plot__(self, u: Expr, v: Expr, w: Expr, ranges: List[List[int]] = None, num: int = 10, title: str = ""):
		x_range = ranges[0]
		y_range = ranges[1]
		if len(ranges) < 3:
			x_range = np.linspace(x_range[0], x_range[1], num)
			y_range = np.linspace(y_range[0], y_range[1], num)
			x, y = np.meshgrid(x_range, y_range)
			u_, v_ = x, y
			for i in range(len(x_range)):
				for j in range(len(y_range)):
					x1 = x[i, j]
					y1 = y[i, j]
					u_[i, j] = u.subs({self.x: x1, self.y: y1})
					v_[i, j] = v.subs({self.x: x1, self.y: y1})
			plt.title(title)
			plt.tick_params(labelleft=False, labelbottom=False)
			plt.quiver(x, y, u_, v_)
			plt.show()
		else:
			x_range = np.linspace(x_range[0], x_range[1], num)
			y_range = np.linspace(y_range[0], y_range[1], num)
			z_range = np.linspace(ranges[2][0], ranges[2][1], num)
			x, y, z = np.meshgrid(x_range, y_range, z_range)
			u_, v_, w_ = x, y, z
			for i in range(len(x_range)):
				for j in range(len(y_range)):
					for k in range(len(z_range)):
						x1 = x[i, j, k]
						y1 = y[i, j, k]
						z1 = z[i, j, k]
						u_[i, j, k] = u.subs({self.x: x1, self.y: y1, self.z: z1})
						v_[i, j, k] = v.subs({self.x: x1, self.y: y1, self.z: z1})
						w_[i, j, k] = w.subs({self.x: x1, self.y: y1, self.z: z1})
			plt.title("3D " + title)
			plt.tick_params(labelleft=False, labelbottom=False)
			plt.quiver(x, y, z, u_, v_, w_)

	def get_summary(self, ranges: List[List[int]], num: int = 10):
		self.__plot__(self.u, self.v, self.w, ranges=ranges, num=num, title="Velocity Field")
		a_x, a_y, a_z = self.get_acceleration_equations()
		self.__plot__(a_x, a_y, a_z, ranges=ranges, num=num, title="Acceleration Field")
		volumetric_strain = self.volumetric_strain_equation()
		shear_strain = self.shear_strain_rate_equation()
		vorticity = self.vorticity_equation()

		return {
			"acceleration": {
				"x": simplify(a_x),
				"y": simplify(a_y),
				"z": simplify(a_z)
			},
			"volumetric strain": simplify(volumetric_strain),
			"shear strain": simplify(shear_strain),
			"vorticity": simplify(vorticity)
		}

