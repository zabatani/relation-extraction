import codecs
import spacy
import sys


def main(argv):
	#input_filename = argv[1]
	input_filename = "data/Corpus.DEV.txt"
	output_filename = "data/output"
	relation_type = "Live_In"
	entity_types = (["PERSON"], ["GPE", "LOC"])
	threshold = 0.7
	nlp = spacy.load('en')
	output_file = open(output_filename, 'w')
	for sent_id, sent_str in read_lines(input_filename):
		sent = nlp(sent_str)
		entitiesA = []
		entitiesB = []
		for ne in sent.ents:
			if ne.root.ent_type_ in entity_types[0]:
				entitiesA.append(ne)
			if ne.root.ent_type_ in entity_types[1]:
				entitiesB.append(ne)
		for entityA in entitiesA:
			for entityB in entitiesB:
				if get_score(sent, entityA, entityB) > threshold:
					output_file.write("{}\t{}\t{}\t{}\t( {})\n".format(sent_id, entityA.text, relation_type, entityB.text, sent_str))

	output_file.close()


def get_score(sent, entityA, entityB):
	# TODO: Dear Alon, this is an example of iterating through the text between the two entities
	#for i in range(entityA.end, entityB.start):
		#print(sent[i].text)
	return 1


def read_lines(filename):
	for line in codecs.open(filename, encoding="utf8"):
		sent_id, sent = line.strip().split("\t")
		sent = sent.replace("-LRB-", "(")
		sent = sent.replace("-RRB-", ")")
		yield sent_id, sent


if __name__ == "__main__":
	main(sys.argv)
