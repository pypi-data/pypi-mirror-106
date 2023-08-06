
import os
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt

def version():
    version = '0.1.4'
    print('perpy version:' + version)

def load(path=None, col_labels=None, scaling=True):
    '''
        load dataset from file

        parameters:
            path: None(default), string
                data file directory
                None: current directory
            col_labels: None(default), number
                None: non labels
                0: the labels is in the first column
                otherwise: the labels is in the last column
            scaling: True(default), False
                True: to max min scaling
                False: no max min scaling

        return:
            (x, labels) / x
            x: samples set
            labels: label set
    '''
    if path is None:
        path = os.getcwd()

    file_names = os.listdir(path)

    # --------------------display list file name----------------

    len_str = 51
    print('|' + '|\n'.rjust(len_str, '-'))

    len_left = len_str // 2 + 11 // 2 - 1
    len_right = len_str // 2 - 11 // 2 + 2

    print('|' + 'choose file'.rjust(len_left, ' ') + '|\n'.rjust(len_right, ' '))
    print('|' + '|\n'.rjust(len_str, '-'))
    for i in range(len(file_names)):
        len_index = len(str(i))
        len_filename = len(file_names[i])
        print('| ' + str(i) + file_names[i].rjust(len_str - len_index - 4, ' ') + ' |\n')

    print('|' + '|\n'.rjust(len_str, '-'))
    n = int(input('Please enter the index of file you will load:'))

    # -------------------load dataset-----------------
    try:
        try:
            x = np.loadtxt(path + '\\' + file_names[n], delimiter=',')
        except:
            x = np.loadtxt(path + '\\' + file_names[n])
    except:
        print('please modify delimiter!')

    # ------------------labels-----------------

    if col_labels is None:
        pass
    elif col_labels == 0:
        true_labels = x[:, 0]
        x = np.delete(x, 0, axis=1)
    else:
        col_labels = x.shape[1] - 1
        true_labels = x[:, col_labels]
        x = np.delete(x, col_labels, axis=1)

    # ------------------scaling------------------

    if scaling is True:
        scaler = MinMaxScaler()
        x = scaler.fit_transform(x)

    if col_labels is None:
        return x
    else:
        return x, true_labels


def dist(A, B):
    '''
        calculate the euclidean distance between point A and point B
    '''
    dist = np.sqrt(np.sum(np.power(A - B, 2)))
    return dist


def plt_scatter(x, labels, axis_show=True, fig_label=[None], fig_legend=None, save=False):
    # -----------------------init-------------------------
    if int(labels.min()) == 1:  # set the number of first label to 0
        labels = labels - 1

    edge_colors = [('tab:blue', '#1f77b4'), ('tab:orange', '#ff7f0e'), ('tab:green', '#2ca02c'),  # edge color list
                   ('tab:red', '#d62728'), ('tab:purple', '#9467bd'), ('tab:brown', '#8c564b'),
                   ('tab:pink', '#e377c2'), ('tab:gray', '#7f7f7f'), ('tab:olive', '#bcbd22'),
                   ('tab:cyan', '#17becf')]

    markers = ['^', '+', '3', 'd', 'x', 'o', 's', 'p']  # marker list

    face_colors = ['none' for i in range(len(markers))]  # face color list

    for i in range(len(face_colors)):
        if markers[i] not in ['^', 'v', 'p', 'o', 's', 'H', 'd', ',', '>', '8', 'h', 'D', '<']:
            face_colors[i] = edge_colors[i][0]

    # -----------------------end-----------------------------

    # ---------------------------x,y-------------------------

    X = [[] for i in range(len(set(labels)))]  # the numbers of cluster
    Y = [[] for i in range(len(x))]

    for i in range(len(labels)):
        X[int(labels[i])].append(x[i][0])
        Y[int(labels[i])].append(x[i][1])

    # ---------------------------end-------------------------

    # ---------------------------draw------------------------
    for i in range(len(X)):
        plt.scatter(X[i], Y[i], c=face_colors[i], edgecolors=edge_colors[i][0], marker=markers[i],
                    label='$' + str(fig_legend[0]) + '_' + str(i) + '$', s=200)

    if fig_legend[0] is not None:  # figure legend
        if fig_legend[1] == '00':
            loc = 'upper left'
        elif fig_legend[1] == '01':
            loc = 'upper right'
        elif fig_legend[1] == '10':
            loc = 'lower left'
        elif fig_legend[1] == '11':
            loc = 'lower right'
        else:
            loc = 'best'

        plt.legend(loc=loc)

    if fig_label is not None:  # figure label
        plt.xlabel(r'$' + fig_label[0] + '$')
        plt.ylabel(r'$' + fig_label[1] + '$')

    # ---------------------------end-------------------------

    if axis_show is False:
        plt.xticks([])
        plt.yticks([])

    # -----------------------save-------------------------

    if save is not False:
        plt.savefig(save[0], dpi=save[1], bbox_inches='tight')

    # ------------------------end-------------------------
    plt.show()


def plt_runtime(times, instances, labels, save=False):
    num_lines = len(times)

    colors = [('tab:blue', '#1f77b4'), ('tab:orange', '#ff7f0e'), ('tab:green', '#2ca02c'),  # edge color list
              ('tab:red', '#d62728'), ('tab:purple', '#9467bd'), ('tab:brown', '#8c564b'),
              ('tab:pink', '#e377c2'), ('tab:gray', '#7f7f7f'), ('tab:olive', '#bcbd22'),
              ('tab:cyan', '#17becf')]

    markers = ['.', '+', '3', 'x']
    linestyles = ['-.', '-', '--', ':']

    fig = plt.figure()
    left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    ax1 = fig.add_axes([left, bottom, width, height])
    for i in range(num_lines):
        ax1.plot(instances, times[i], c=colors[i][0], label=labels[i], marker=markers[i], linestyle=linestyles[i])

    ax1.set_xlabel("$Instances$")
    ax1.set_ylabel("$Runtime(s)$")

    ax1.legend()

    if save is not False:
        plt.savefig(save[0], dpi=save[1], bbox_inches='tight')

    plt.show()


def plt_radar(labels, data, algorithm, title=None, legend=None, save=False):
    num_labels = len(labels)
    num_data = data.shape[0]
    angles = np.linspace(0, 2 * np.pi, num_labels, endpoint=False)

    num_algorithm = data.shape[1]
    current_data = np.zeros((num_data, num_algorithm + 1))

    for i in range(num_data):
        current_data[i] = np.concatenate((data[i], [data[i][0]]))

    angles = np.concatenate((angles, [angles[0]]))
    labels = np.concatenate((labels, [labels[0]]))

    for i in range(num_data):
        plt.polar(angles, current_data[i], 'o-', linewidth=1, label='$' + algorithm[i] + '$')
        plt.fill(angles, current_data[i], alpha=0.25)

    plt.thetagrids(angles * 180 / np.pi, labels)

    if title is not None:
        plt.title('$' + title + '$')
    if legend is not None:
        plt.legend(bbox_to_anchor=(legend))

    if save is not False:
        plt.savefig(save[0], dpi=save[1], bbox_inches='tight')

    plt.show()

def main():
    pass


if __name__ == '__main__':
    main()