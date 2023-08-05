import wandb
from ray.tune import report


PREFIX = 'small_space_522_'

def initialize_logging(config):
    wandb.init(project='Edet')
    wandb.run.name = PREFIX + wandb.run.name
    wandb.config.update(config)


def extract_scores(history):
    scores = history.history

    for key in scores.keys():
        scores[key] = scores[key][0]

    return scores


def report_scores(history):
    scores = extract_scores(history)
    wandb.log(scores)
    report(
        loss=scores['val_loss'],
        classification_loss=scores['val_classification_loss'],
        regression_loss=scores['val_regression_loss'])
        
