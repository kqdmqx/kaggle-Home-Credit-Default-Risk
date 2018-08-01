import os
import glob


def get_path(header):
    items = header.split("/")
    return "/".join(items[:-1])


def raw_filename(filename):
    return filename.split(".")[0]


def get_id(part):
    if "_" not in part:
        return 0
    return int(part.split("_")[-1])


def incremental_path(path, header, info):
    schema = os.path.join(path, header)
    filenames = [f_.replace("\\", "/") for f_ in glob.glob(schema + "*")]
    schema_len = len(schema)
    tail_filenames = [raw_filename(f_[schema_len:]) for f_ in filenames]
    max_id = max([get_id(tail_) for tail_ in tail_filenames]) + 1 if len(tail_filenames) > 0 else 0
    return "{}_{}_{}".format(schema, info, max_id)


if __name__ == '__main__':
    path = "D:/git/kaggle-Home-Credit-Default-Risk/neptune-features/"
    header = "nothing"
    print(incremental_path(path, header, "info"))
