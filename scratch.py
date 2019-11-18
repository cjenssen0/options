import matplotlib.pyplot as plt
plt.imshow(v[:,53].reshape(10,10))
plt.colorbar()
plt.show()

plt.stem(scores)
plt.show()

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
# Make data.
#vi = self.eigenvectors[:,0]
vi = eigenvectors[:,0]
#vi = v[:,99]
X = np.arange(13)
Y = np.arange(13)
X, Y = np.meshgrid(Y, X)
Z = vi.reshape(13,13)

fig = plt.figure()
ax = fig.gca(projection='3d')

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.viridis)
plt.show()

##
vi = v[:,53]
plt.imshow(vi.reshape(10,10))
plt.show()

#------PLOTS------#
#Plot Ip
plt.stem(scores)
plt.xlabel("i")
plt.ylabel("V")
plt.title("Stem plot of scores for kernel=np.exp(-(L) / 2.0)")
plt.show()

#Plot eigvals
plt.stem(w)
plt.xlabel("i")
plt.ylabel("lambda")
plt.title("Stem plot of sorted eigenvalues for kernel=np.exp(-(L) / 2.0)")
plt.show()

#--Plot eigenvectors
i = 0
fig, axs = plt.subplots(2, 2)
axs[0, 0].imshow(self.eigenvectors[:,i].reshape(10,10), cmap="viridis")
axs[0, 0].set_title('1st eigenvector')
axs[0, 1].imshow(self.eigenvectors[:,i+1].reshape(10,10))
axs[0, 1].set_title('2nd eigenvector')
axs[1, 0].imshow(self.eigenvectors[:,i+2].reshape(10,10))
axs[1, 0].set_title('3rd eigenvector')
axs[1, 1].imshow(self.eigenvectors[:,i+3].reshape(10,10))
axs[1, 1].set_title('4th eigenvector')
#fig.colorbar(axs, ax=axs.ravel().tolist())

for ax in axs.flat:
    ax.set(xlabel='x', ylabel='y')
    #fig.colorbar(ax, ax=axs.ravel().tolist())
# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()
plt.show()

#--
#plt.stem(eigenvectors.sum(0))
#plt.imshow(eigenvectors[:, -1].reshape(13, 13))
plt.figure(1)
for i in range(64):
    plt.subplot(8, 8, i+1)
    plt.plot(eigenvectors[:, -i])	
    plt.title(i)

plt.figure(3)
for i in range(64):
    plt.subplot(8, 8, i+1)
    plt.plot(eigenvectors[:, i])	
    plt.title(i)

#plt.figure(2)
#plt.stem(eigenvectors.sum(0))
#plt.show()
#raise
#--


#---------------
eigenvalues, eigenvectors = np.linalg.eigh(normalizedL)
# I need to sort the eigenvalues and eigenvectors
#idx = eigenvalues.argsort()[::-1]
v_sum = np.dot(eigenvectors.T, np.ones_like(eigenvalues))
scores = (np.sqrt(eigenvalues)*v_sum)**2
idx = np.argsort(scores)