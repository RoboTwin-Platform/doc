# Collect Data

We provide over 100,000 pre-collected trajectories as part of the open-source release [RoboTwin Dataset](https://huggingface.co/datasets/TianxingChen/RoboTwin2.0/tree/main/dataset). **We recommend downloading the pre-collected XPolicyLab-format data (step 1) as the default path** — it is ready to train on immediately. Collect data yourself (step 2) only when you need custom task configs, domain randomization, or embodiment setups.

Before collecting or evaluating, please review common issue #3, [Stuck While Collecting Data and Evaluating](../common-issue/index.md). We strongly recommend avoiding A-, H-, or V-series GPUs for data collection and policy evaluation.

## 1. Download XPolicyLab-Format Data (Recommended)

Download and extract all available XPolicyLab-format trajectories from Hugging Face:

```bash
bash scripts/download_xpolicylab_data.sh
```

To download only selected tasks, pass their names:

```bash
bash scripts/download_xpolicylab_data.sh adjust_bottle beat_block_hammer
```

Downloads land under `data/RoboTwin/<task_name>/aloha_agilex/data/` (note: self-collected data lands under `data/<task_config>/...` instead).

## 2. Task Running and Data Collection (Optional)

For custom task configs, domain randomization, or embodiment setups, collect data yourself. Running the following command will first search for a random seed for the target collection quantity, and then replay the seed to collect data.

```bash
bash collect_data.sh ${task_name} ${task_config} ${gpu_id}
# Clean Data Example: bash collect_data.sh beat_block_hammer demo_clean 0
# Randomized Data Example: bash collect_data.sh beat_block_hammer demo_randomized 0
```

Collected demonstrations are saved **directly in the XPolicyLab trajectory format** — no extra conversion step is needed:

```text
data/<task_config>/<task_name>/<embodiment>/data/episode_0000000.hdf5
```

`<embodiment>` follows the `embodiment` field of the task config (`aloha_agilex` for the default `aloha-agilex` setup).

All available `task_name` options can be found in the [tasks documentation](../tasks/index.md). The `gpu_id` parameter specifies which GPU to use and should be set to an integer in the range `0` to `N-1`, where `N` is the number of GPUs available on your system.

Our data synthesizer enables automated data collection by executing the task scripts in the `envs` directory, in combination with the `curobo` robot planner. Specifically, data collection is configured through a task-specific configuration file (see [Configurations](configurations.md)), which defines parameters such as the target embodiment, domain randomization settings, and the number of data samples to collect.

The success rate of data generation for each embodiment across all tasks can be found at: [50 Bimanual Tasks](../tasks/index.md). Due to the structural limitations of different robotic arms, not all embodiments are capable of completing every task.

Our pipeline first explores a set of random seeds (`seed.txt`) to identify trajectories that can yield successful data collection. It then records fine-grained action trajectories (`_traj_data`) accordingly. Collected videos are available in the `videos` directory.

The entire process is fully automated—just run a single command to get started.

> ⚠️ The `missing pytorch3d` warning can be ignored if 3D data is not required.

### Migrating data collected with older RoboTwin versions

Data collected before the XPolicyLab-native format landed used the legacy raw layout `data/<task_name>/<task_config>/data/episode0.hdf5`. `scripts/process_data_xpolicylab.py` converts that legacy layout only; it is not needed for (and does not work on) freshly collected data.

```bash
python scripts/process_data_xpolicylab.py \
  <task_name> <task_config> [episode_num] --overwrite

# Example
python scripts/process_data_xpolicylab.py \
  adjust_bottle demo_clean 1 --overwrite
```

To convert every collected task/config under `data/`:

```bash
python scripts/process_data_xpolicylab.py --all --overwrite
```

### Decoding images from HDF5

Images may be stored as encoded bit streams. Prefer the XPolicyLab helper (it handles legacy layouts correctly):

```python
from XPolicyLab.utils.process_data import decode_image_bit

image = decode_image_bit(image_bit)
```
