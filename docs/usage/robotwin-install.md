# Install & Download
## **Dependencies**

System Support: 

We currently best support Linux based systems. There is limited support for windows and no support for MacOS at the moment. We are working on trying to support more features on other systems but this may take some time. Most constraints stem from what the [SAPIEN](https://github.com/haosulab/SAPIEN/) package is capable of supporting.

| System / GPU         | CPU Sim | GPU Sim | Rendering |
| -------------------- | ------- | ------- | --------- |
| Linux / NVIDIA GPU   | ✅      | ✅      | ✅        |
| Windows / NVIDIA GPU | ✅      | ❌      | ✅        |
| Windows / AMD GPU    | ✅      | ❌      | ✅        |
| WSL / Anything       | ✅      | ❌      | ❌        |
| MacOS / Anything     | ✅      | ❌      | ✅        |


> Occasionally, data collection may get stuck when using A/H series GPUs. This issue may be related to [RoboTwin issue #83](https://github.com/RoboTwin-Platform/RoboTwin/issues/83#issuecomment-3012135745) and [SAPIEN issue #219](https://github.com/haosulab/SAPIEN/issues/219).

Python versions:

* Python 3.10

CUDA version:

* 12.1 (Recommended)

Hardware:

* Rendering: NVIDIA or AMD GPU

* Ray tracing: NVIDIA RTX GPU or AMD equivalent

* Ray-tracing Denoising: NVIDIA GPU

* GPU Simulation: NVIDIA GPU

Software:

* Ray tracing: NVIDIA Driver >= 470
* Denoising (OIDN): NVIDIA Driver >= 520

### Additional Requirements for Docker

When running in a Docker container, ensure that the following environment variable is set when starting the container:

```bash
-e NVIDIA_DRIVER_CAPABILITIES=compute,utility,graphics
```

Important : The graphics capability is essential. Omitting it may result in segmentation faults due to missing Vulkan support.

For more information, see [HERE](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/docker-specialized.html).

## Install Vulkan (if not installed)
```
sudo apt install libvulkan1 mesa-vulkan-drivers vulkan-tools
```
Check by running `vulkaninfo`


## Basic Env
First, prepare a conda environment.
```bash
conda create -n RoboTwin python=3.10 -y
conda activate RoboTwin
```

RoboTwin 2.0 Code Repo: [https://github.com/RoboTwin-Platform/RoboTwin](https://github.com/RoboTwin-Platform/RoboTwin)

XPolicyLab is embedded as a Git submodule. For a fresh checkout, clone RoboTwin recursively:

```bash
git clone --recurse-submodules https://github.com/RoboTwin-Platform/RoboTwin.git
cd RoboTwin
```

For an existing checkout, initialize the version pinned by RoboTwin:

```bash
git submodule update --init --recursive XPolicyLab
```

To pull the latest XPolicyLab commit on its configured `main` branch and refresh RoboTwin's submodule pin:

```bash
bash scripts/update_xpolicylab.sh
# optional: stage the pin / reinstall the editable package
bash scripts/update_xpolicylab.sh --stage --install
```

Then, run `scripts/_install.sh` to install basic envs and CuRobo:
```
bash scripts/_install.sh
```

If you meet curobo config path issue, try to run `python scripts/update_embodiment_config_path.py`

If you encounter any problems, please refer to the [manual installation](#manual-installation-only-when-step-2-failed) section. If you are not using 3D data, a failed installation of pytorch3d will not affect the functionality of the project.

If you haven't installed ffmpeg, please turn to [https://ffmpeg.org/](https://ffmpeg.org/). Check it by running `ffmpeg -version`.

## Download Assets (RoboTwin-OD, Texture Library and Embodiments)
To download the assets, run the following command. If you encounter any rate-limit issues, please log in to your Hugging Face account by running `huggingface-cli login`:
```
bash scripts/_download_assets.sh
```

The structure of the `assets` folder should be like this:

```text
assets
├── background_texture
├── embodiments
│   ├── embodiment_1
│   │   ├── config.yml
│   │   └── ...
│   └── ...
├── objects
└── ...
```

## Manual Installation (Only when step 3 failed)
1. Install requirements
```bash
pip install -r scripts/requirements.txt
```

2. Install pytorch3d
```bash
pip install "git+https://github.com/facebookresearch/pytorch3d.git@stable"
```

3. Install CuRobo
```
cd envs
git clone https://github.com/NVlabs/curobo.git
cd curobo
pip install -e . --no-build-isolation
cd ../..
```

4. Adjust code in `mplib` (**Important**)
- You can use `pip show mplib` to find where the `mplib` installed.

- Remove `or collide`

```python
# mplib.planner (mplib/planner.py) line 807
# remove `or collide`

if np.linalg.norm(delta_twist) < 1e-4 or collide or not within_joint_limit:
                return {"status": "screw plan failed"}
=>
if np.linalg.norm(delta_twist) < 1e-4 or not within_joint_limit:
                return {"status": "screw plan failed"}
```


