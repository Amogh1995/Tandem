import draftable
import glob
import os
basepath=os.path.dirname(os.path.abspath('..'))

def comparepdf():
    global f, f1
    path = basepath + "/krait/krait/krait/media/files/input/"
    path1 = basepath + "/krait/krait/krait/media/files/output/"
    client = draftable.Client('dIpzlp-test', 'dcf607f9ba95a9fd6b40bd661b2b06db')
    comparisons = client.comparisons
    #print basepath,path
    for filename in glob.glob(os.path.join(path, '*.pdf')):
        print "@@@@@@"
        print filename
    #\krait\media\files
        f = open(filename, "rb")
    print path1
    for filename1 in glob.glob(os.path.join(path1, '*.pdf')):
        print "!!!!!!"
        print filename1
        f1=open(filename1, "rb")
    comparison = comparisons.create(
        left = comparisons.side_from_file (f, file_type='pdf'),
        right = comparisons.side_from_file (f1, file_type='pdf'),
    )

    print("Comparison created:", comparison)
    print("Viewer URL (expires in 30 min):", comparisons.signed_viewer_url(comparison.identifier))
    return comparisons.signed_viewer_url(comparison.identifier)
