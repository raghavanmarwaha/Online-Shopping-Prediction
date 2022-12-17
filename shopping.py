import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")

def monthToNum(shortMonth):
    return {
            'Jan': 0,
            'Feb': 1,
            'Mar': 2,
            'Apr': 3,
            'May': 4,
            'June': 5,
            'Jul': 6,
            'Aug': 7,
            'Sep': 8, 
            'Oct': 9,
            'Nov': 10,
            'Dec': 11
    }[shortMonth]

def VisitorToNum(short):
    return {
            'Returning_Visitor': 1,
            'New_Visitor': 0,
            'Other': 0,
    }[short]

def TrueToNum(short):
    return {
            'TRUE': 1,
            'FALSE': 0,
    }[short]
    
def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    evidence=[]
    label=[]
    i=-1
    with open(filename,newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            if i==-1:
                i+=1
                continue
            array=row[0].split(',')
            l=[]
            l.append(int(array[0]))
            l.append(float(array[1]))
            l.append(int(array[2]))
            l.append(float(array[3]))
            l.append(int(array[4]))
            l.append(float(array[5]))
            l.append(float(array[6]))
            l.append(float(array[7]))
            l.append(float(array[8]))
            l.append(float(array[9]))
            # month
            l.append(int(monthToNum(array[10])))
            l.append(int(array[11]))
            l.append(int(array[12]))
            l.append(int(array[13]))
            l.append(int(array[14]))
            # visitortype
            l.append(int(VisitorToNum(array[15])))
            # Weekend
            l.append(int(TrueToNum(array[16])))
            evidence.append(l)
            label.append(int(TrueToNum(array[17])))
    return (evidence,label)
            

def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    neigh = KNeighborsClassifier(n_neighbors=1)
    neigh.fit(evidence, labels)
    return neigh


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificty).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    pos=0
    tpos=0
    neg=0
    tneg=0
    l=len(labels)
    for i in range(0,l):
        if(labels[i]==1):
            tpos+=1
        if(labels[i]==0):
            tneg+=1
        if(labels[i]==predictions[i]):
            if(labels[i]==1):
                pos+=1
            else:
                neg+=1
    
    return (pos/tpos,neg/tneg)


if __name__ == "__main__":
    main()
