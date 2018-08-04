import sys


def main(argv):
	#gold_filename = argv[1]
	#predicted_filename = argv[2]
	gold_filename = "data/DEV.annotations"
	predicted_filename = "data/output"
	relation_type = "Live_In"

	gold_labels = get_labels_set(gold_filename, relation_type)
	predicted_labels = get_labels_set(predicted_filename, relation_type)

	# Error Analysis
	precison_errors = predicted_labels - gold_labels
	recall_errors = gold_labels - predicted_labels

	print("Error Analysis\nPrecision Errors:\n{}\nRecall Errors:\n{}".format(precison_errors, recall_errors))

	precision = len(gold_labels & predicted_labels) / len(predicted_labels)
	recall = len(gold_labels & predicted_labels) / len(gold_labels)
	f1 = 2 * (precision * recall) / (precision + recall)
	print("Precision: {}\nRecall: {}\nF1: {}".format(precision, recall, f1))


def get_labels_set(filename, relation_type):
	labels = set()
	with open(filename, 'r') as file:
		for line in file:
			tokens = line.split("\t")
			if tokens[2] == relation_type:
				labels.add((tokens[0], tokens[1], tokens[3]))
	return labels


if __name__ == "__main__":
	main(sys.argv)
