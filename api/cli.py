from api import sportAPI as api, charter as ch

if __name__ == '__main__':
    print("CLI for Bebot!")
    # read file
    api.load_predictions()
    with open('../data/head_to_head_data140005.json', 'r') as myfile:
        data = myfile.read()

    ch.plot_head_to_head_stats(data)