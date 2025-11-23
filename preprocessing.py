import spacy

def tags_and_lemmas(file):
  wordforms = []
  tags = []
  lemmas = []

  # Load a pre-trained English model
  nlp = spacy.load("en_core_web_sm")
  # Apply the model to your data
  doc = nlp(file)
  
  # Extract wordforms, tags and lemmas
  for token in doc:
    if token.is_space or token.is_punct: # is_punct = Viðbót frá nemanda
      continue
    else:
      wordforms.append(token.text)
      tags.append(token.tag_)
      lemmas.append(token.lemma_)
  
  return wordforms, tags, lemmas


def main():
	print("Collecting data from input file.")

	with open("data_eng.txt", "r") as infile:
		infile = infile.read()
		w, t, l = tags_and_lemmas(infile)

	united = zip(w,t,l)

	print("Writing output file.")

	with open("output.txt", "w+") as outfile:
		for w,t,l in united:
			outfile.write(w+"\t"+t+"\t"+l+"\n")

	print("Output file written.")


if __name__ == '__main__':
  main()