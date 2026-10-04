from sklearn.model_selection import train_test_split


def split_data(features, target, test_size: float = 0.2, random_state: int = 42):
    return train_test_split(
        features, target, test_size=test_size, random_state=random_state, stratify=target
    )
