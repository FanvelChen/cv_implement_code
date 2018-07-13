import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import t


def read_test_acc(path):
    acc_list = []
    with open(path) as f:
        for i,line in enumerate(f):
            if i%2 == 1:
                acc_list.append(float(line[-13:-7]))
                # print(line[-13:-7])
    return np.array(acc_list)

def main():
    # 样本大小
    n = 1000

    test_acc = read_test_acc('record.txt')
    heng = []
    for i in range(test_acc.size):
        heng.append(i*100)
    heng = np.array(heng)
    # print(heng)


    # 95% Confidence Interval

    # dof = n - 1         # degrees of freedom
    # alpha = 1.0 - 0.95
    # conf_interval = t.ppf(1-alpha/2., dof) * test_acc_std*np.sqrt(1.+1./n)


    fig = plt.gca()
    # plt.errorbar(heng, test_acc, yerr=conf_interval, fmt='-',)
    plt.plot(heng,test_acc)


    plt.xlim([-100,heng.max()+100])
    plt.ylim(0, 1.08)

    # axis formatting
    fig.spines["top"].set_visible(False)
    fig.spines["right"].set_visible(False)
    plt.tick_params(axis="both", which="both", bottom="off", top="off",
                    labelbottom="on", left="on", right="off", labelleft="on")

    # plt.legend(['Acc'],
    #            loc='lower right',
    #            numpoints=1,
    #            fancybox=True)

    plt.ylabel('Acc')
    plt.xlabel('Steps')
    plt.title('5-way 1-shot Acc')

    plt.show()

if __name__ == '__main__':
    main()



