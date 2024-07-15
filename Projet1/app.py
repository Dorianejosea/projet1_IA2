from descriptor import glcm, bitdesc

path = 'Projet1_Dataset/COVID-CT-master'
path1 = 'Projet1_Dataset/-Glaucoma'
path2 = 'Projet1_Dataset/Iris'
path3 = 'Projet1_Dataset/KTH-TIPS2-a'
path4 = 'Projet1_Dataset/Outex24'
path5 = 'Projet1_Dataset/Satelite_dataset'
path6 = 'Projet1_Dataset/Wildfire_detection'

def main():
    
    feat_glcm = glcm(path)
    feat_bit = bitdesc(path)
    feat_glcm = glcm(path1)
    feat_bit = bitdesc(path1)
    feat_glcm = glcm(path2)
    feat_bit = bitdesc(path2)
    feat_glcm = glcm(path3)
    feat_bit = bitdesc(path3)
    feat_glcm = glcm(path4)
    feat_bit = bitdesc(path4)
    feat_glcm = glcm(path5)
    feat_bit = bitdesc(path5)
    feat_glcm = glcm(path6)
    feat_bit = bitdesc(path6)
    
    print(f'GLCM\n-----\n{feat_glcm}')
    print(f'BiT\n---\n{feat_bit}')

if __name__ == '__main__':
    main()