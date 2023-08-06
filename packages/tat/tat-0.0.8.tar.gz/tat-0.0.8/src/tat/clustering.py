import numpy as np
from skimage import filters
from sklearn.cluster import KMeans
import time
import mimetypes


class Tat:
    @staticmethod
    def guess_type(filename):
        filetype = mimetypes.guess_type(filename)[0]
        if filetype is None:
            return None
        return filetype.split("/")[0]

    @staticmethod
    def is_image(filename):
        return Tat.guess_type(filename) == "image"

    @staticmethod
    def generate_layers(src_image: np.ndarray, cluster_count: int, run_count: int, max_iter_count: int):
        img_shape = src_image.shape
        start_time = time.time()
        k_means = KMeans(n_clusters=cluster_count, random_state=0, n_init=run_count, max_iter=max_iter_count).fit(
            filters.gaussian(src_image.reshape(img_shape[0] * img_shape[1], 1), 2))
        delta = time.time() - start_time
        print(f"k-means computing time: {delta}")
        segments = k_means.labels_.reshape(img_shape)
        labeled_segments = k_means.cluster_centers_[segments][:, :, 0]
        labeled_cluster = np.asarray(k_means.cluster_centers_)

        powers = np.floor(np.log10(labeled_segments))
        monochrome_labeled_segments = 100 ** powers * np.floor(labeled_segments / 100 ** powers)

        powers_cluster = np.floor(np.log10(labeled_cluster))
        monochrome_labeled_cluster = np.sort(100 ** powers_cluster * np.floor(labeled_cluster / 100 ** powers_cluster),
                                             axis=0)

        layers = []
        for i in range(len(monochrome_labeled_cluster)):
            layer = np.zeros(shape=np.shape(monochrome_labeled_segments)).astype(np.uint8)
            layer[monochrome_labeled_segments == monochrome_labeled_cluster[i]] = 1
            layers.append(layer)
        return layers, monochrome_labeled_segments
