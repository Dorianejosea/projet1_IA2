from descriptor import glcm, bitdesc
from distances import manhattan, euclidean, chebyshev, canberra

path = 'Projet1_Dataset/COVID-CT-master'
path1 = 'Projet1_Dataset/-Glaucoma'
path2 = 'Projet1_Dataset/Iris'
path3 = 'Projet1_Dataset/KTH-TIPS2-a'
path4 = 'Projet1_Dataset/Outex24'
path5 = 'Projet1_Dataset/Satelite_dataset'
path6 = 'Projet1_Dataset/Wildfire_detection'


def main():
    
    feat_path = glcm(path)
    feat_path1 = glcm(path1)
    feat_path2 = glcm(path2)
    feat_path3 = glcm(path3)
    feat_path4 = glcm(path4)
    feat_path5 = glcm(path5)
    feat_path6 = glcm(path6)


    print(f'''\nManhattan: {manhattan(feat_path, feat_path1)} | {manhattan(feat_path, feat_path2)} | {manhattan(feat_path, feat_path3)} | {manhattan(feat_path, feat_path4)} | {manhattan(feat_path, feat_path5)} | {manhattan(feat_path, feat_path6)}\n
                         Euclidean: {euclidean(feat_path, feat_path1)} | {euclidean(feat_path, feat_path2)}  | {euclidean(feat_path, feat_path3)} | {euclidean(feat_path, feat_path4)} | {euclidean(feat_path, feat_path5)} | {euclidean(feat_path, feat_path6)}\n
                         Chebyshev: {chebyshev(feat_path, feat_path1)} | {chebyshev(feat_path, feat_path2)}  | {chebyshev(feat_path, feat_path3)} | {chebyshev(feat_path, feat_path4)} | {chebyshev(feat_path, feat_path5)} | {chebyshev(feat_path, feat_path6)}\n
                         Canberra: {canberra(feat_path, feat_path1)} | {canberra(feat_path, feat_path2)}  | {canberra(feat_path, feat_path3)} | {canberra(feat_path, feat_path4)} | {canberra(feat_path, feat_path5)} | {canberra(feat_path, feat_path6)}\n
                            ''')

if __name__ == '__main__':
    main()