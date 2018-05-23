

def num(word, sentence_words):
    count = 0
    for w in sentence_words:
        if word == w:
            count += 1
    
    return count


def spectrum_kernel_value(question_words, sentence_words):
    kernel_value = 0
    vocab_inters = set(question_words).intersection(sentence_words)
    
    for word in vocab_inters:
        kernel_value += num(word, question_words) * num(word, sentence_words)
        
    return kernel_value


def presence_kernel_value(question_words, sentence_words):
    kernel_value = 0
    vocab_inters = set(question_words).intersection(sentence_words)
    
    return len(vocab_inters)


def intersection_kernel_value(question_words, sentence_words):
    kernel_value = 0
    vocab_inters = set(question_words).intersection(sentence_words)
    
    for word in vocab_inters:
        kernel_value += min(num(word, question_words), num(word, sentence_words))
        
    return kernel_value


def kernel_solution(question_words, context_sentences, kernel_type='intersection_kernel'):
    scores = {}
    
    for sentence_label in range(len(context_sentences)):
        kernel_value = 0
        if kernel_type == 'spectrum_kernel':
            kernel_value = spectrum_kernel_value(question_words, context_sentences[sentence_label])
        elif kernel_type == 'presence_kernel':
            kernel_value = presence_kernel_value(question_words, context_sentences[sentence_label])
        elif kernel_type == 'intersection_kernel':
            kernel_value = intersection_kernel_value(question_words, context_sentences[sentence_label])
        
        scores[sentence_label] = kernel_value
        
    labels = sorted(scores, key=scores.get, reverse=True)
    
    return labels


def run_method(method, question_words, candidate_answers_words):
    if method == 'random_solution':
        return random_solution(len(candidate_answers_words))
    elif 'kernel' in method:
        return kernel_solution(question_words, candidate_answers_words, method)
    elif 'sentence_similarity' in method:
        return sentence_similarity_solution(question_words, candidate_answers_words)
    
    return None


def run(dataset, method='random_solution'):
    results = {'Method': method, 'Prec@1': [], 'Prec@5': [], 'Prec@10': [],
               'AvgPrec': [], 'MAP': 0}
    idx = 0
    for article in dataset['data']:
        for qas_context in article['paragraphs']:
            # get the number of candidate answers
            nr_candidate_answers = qas_context['nr_candidate_answers']

            for qas in qas_context['qas']:
                # get answers' labels from context
                answer_labels = list()
                for answer in qas['answers']:
                    answer_labels.append(answer['answer_label'])
                    
                # trying to keep the same notation
                question_words = qas['question_words']
                candidate_answers_words = qas_context['context_sentences_words']
                y = answer_labels
                
                # run a method
                y_pred = run_method(method, question_words, candidate_answers_words)
                
                # evaluation
                results['Prec@1'].append(evaluation.precision_at_k(y_pred, y, k=1))
                #results['Prec@5'].append(evaluation.precision_at_k(y_pred, y, k=5))
                #results['Prec@10'].append(evaluation.precision_at_k(y_pred, y, k=10))
                results['AvgPrec'].append(evaluation.average_precision(y_pred, y))
                
                '''
                if idx == 414:
                    print('idx: {}\n'.format(idx))
                    print('question: {}\n'.format(question))
                    print('candidate_answers:')
                    pprint(candidate_answers)
                    print('context length', len(qas_context['context']))
                    print('context_sentences sum(length)', np.sum([len(s) for s in qas_context['context_sentences']]))
                    for answer in qas['answers']:
                        print('answer_start', answer['answer_start'])
                    print('y_pred: {}\n'.format(y_pred))
                    print('y: {}\n'.format(y))
                '''
                
                idx += 1
                '''
                if idx % 10000 == 0:
                    print('{}'.format(idx))
                '''
                         
                
    # evaluation (MAP - mean average precision)
    results['MAP'] = np.mean(results['AvgPrec'])
    results['StdAP'] = np.std(results['AvgPrec'])
    results['AvgPrec@1'] = np.mean(results['Prec@1'])
    results['StdPrec@1'] = np.std(results['Prec@1'])
    #results['AvgPrec@5'] = np.mean(results['Prec@5'])
    #results['AvgPrec@10'] = np.mean(results['Prec@10'])
    
    return results