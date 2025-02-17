# Run this file from the root directory with the terminal command `mpiexec -n 4 python sample_solutions/essay_word_counter.py`

import string
import mpi4py.MPI as MPI


def count_word_occurrences_in_file(file_path):
    '''
    Count the occurrences of each word in a file.
    
    Args:
        file_path (str): The path to the file to analyze.
        
    Returns:
        dict: A dictionary where the keys are the words in the file and the values are the number of times each word appears.
    '''
    with open(file_path, 'r') as file:
        # Get the text from the file as a string
        text = file.read()

    # Convert the text to lowercase and remove punctuation
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Split the text into a list of words
    words = text.split()    

    # Create a dictionary to store the word occurrences
    word_occurrences = {}
    for word in words:
        # Add the word to the dictionary if it doesn't exist, otherwise increment the count
        if word in word_occurrences:
            word_occurrences[word] += 1
        else:
            word_occurrences[word] = 1

    return sort_dict_by_value(word_occurrences)


def sort_dict_by_value(d):
    '''
    Sort a dictionary by its values in descending order.

    Args:
        d (dict): The dictionary to sort.

    Returns:
        dict: The sorted dictionary.
    '''
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))


def form_filepath(i):
    '''
    Form the file path for the essay with index i.

    Args:
        i (int): The index of the essay.

    Returns:
        str: The file path for the essay
    '''
    return f'data/07_essays/essay_{str(i).zfill(3)}.txt'


def add_dictionaries(d1, d2):
    '''
    Add two dictionaries together.

    Args:
        d1 (dict): The first dictionary.
        d2 (dict): The second dictionary.

    Returns:
        dict: The combined dictionary.
    '''
    # Initialize the combined dictionary
    combined_dict = d1.copy()

    # Add the values from the second dictionary to the first dictionary
    for key, value in d2.items():
        if key in combined_dict:
            combined_dict[key] += value
        else:
            combined_dict[key] = value

    return combined_dict


# This is a new function which will be called on each rank to count the words in a range of essays
def count_words_in_essays(i_first, i_last):
    '''
    Count the occurrences of each word in a range of essays.

    Args:
        i_first (int): The index of the first essay.
        i_last (int): The index of the last essay.

    Returns:
        dict: A dictionary where the keys are the words in the essays and the values are the number of times each word appears.
    '''
    # Initialize the total word count dictionary
    total_word_count = {}

    # Loop over the range of essays
    for i in range(i_first, i_last + 1):
        # Get the file path for the current essay
        file_path = form_filepath(i)

        # Count the word occurrences in the current essay
        word_count = count_word_occurrences_in_file(file_path)

        # Add the word occurrences from the current essay to the total word count
        total_word_count = add_dictionaries(total_word_count, word_count)

    return total_word_count


# We use MPI to parallelize the word counting process
# The following code will be excuted in each rank

# Get the rank and number of ranks
rank = MPI.COMM_WORLD.Get_rank()
n_rank = MPI.COMM_WORLD.Get_size()

# Define the range of essays to analyze
i_max = 999
i_first = int(rank * (i_max + 1) / n_rank)
i_last = int((rank + 1) * (i_max + 1) / n_rank) - 1

# Count the word occurrences in the range of essays
# By counting words and combining on each rank we reduce the amount of information that needs to be gathered to and processed on rank 0
# Call the new function written above
word_count = count_words_in_essays(i_first, i_last)

# Gather the word counts from all ranks to rank 0
word_counts = MPI.COMM_WORLD.gather(word_count, root=0)

if rank == 0:
    # The data is all on rank 0
    # Combine the word counts from all ranks
    total_word_count = {}
    for wc in word_counts:
        total_word_count = add_dictionaries(total_word_count, wc)

    # Sort the word counts by the number of occurrences
    # There was no point in sorting the word count on each rank, as we need to sort the total word count
    total_word_count = sort_dict_by_value(total_word_count)

    # Print the word counts
    print(total_word_count)

