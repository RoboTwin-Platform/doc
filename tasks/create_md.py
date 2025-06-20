import os
import yaml
import json
import pdb

def load_yml(yml_file):
    with open(yml_file, 'r') as file:
        return yaml.safe_load(file)

def load_json(json_file):
    with open(json_file, 'r') as file:
        return json.load(file)

# save html file
def save_html_file(save_path, data):
    """
    Save HTML content to a file.
    
    Args:
        data (str): HTML content to save.
        save_path (str): Path where the HTML file will be saved.
    """
    with open(save_path, 'w', encoding='utf-8') as file:
        file.write(data)
    print(f"HTML file saved to {save_path}")

def get_embodiments_success_rates(task_name):
    # from txt files read all embodimentsall success rates on tasks
    success_rates = {
        'ALOHA': 0,
        'X5': 0,
        'FRANKA': 0,
        'PIPER': 0,
        'UR5': 0
    }
    with open(f'./all_tasks_success_rates.txt', 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        if line[:len(task_name)] == task_name and line[len(task_name)] == " ":
            # the rate is splited by some spaces
            rates = line[len(task_name):].strip().split()
            for id, key in enumerate(success_rates.keys()):
                success_rates[key] = int(float(rates[id])*100)
            return success_rates
    print(f"No {task_name} in all_tasks_success_rates.txt")
    return success_rates

if __name__ == "__main__":
    task_list = [
        "adjust_bottle",
        "beat_block_hammer",
        "blocks_ranking_rgb",
        "blocks_ranking_size",
        "click_alarmclock",
        "click_bell",
        "dump_bin_bigbin",
        "grab_roller",
        "handover_block",
        "handover_mic",
        "hanging_mug",
        "lift_pot",
        "move_can_pot",
        "move_playingcard_away",
        "move_stapler_pad",
        "open_laptop",
        "open_microwave",
        "pick_diverse_bottles",
        "pick_dual_bottles",
        "place_a2b_left",
        "place_a2b_right",
        "place_bread_basket",
        "place_bread_skillet",
        "place_can_basket",
        "place_cans_plasticbox",
        "place_container_plate",
        "place_dual_shoes",
        "place_empty_cup",
        "place_fan",
        "place_mouse_pad",
        "place_object_scale",
        "place_object_stand",
        "place_phone_stand",
        "place_shoe",
        "place_object_basket",
        "put_bottles_dustbin",
        "put_object_cabinet",
        "rotate_qrcode",
        "scan_object",
        "shake_bottle_horizontally",
        "shake_bottle",
        "stack_blocks_three",
        "stack_blocks_two",
        "stack_bowls_three",
        "stack_bowls_two",
        "stamp_seal",
        "turn_switch",
        "move_pillbottle_pad",
        "place_burger_fries",
        "press_stapler"
    ]

    task_list = sorted(task_list)
    # for task in task_list:
    #     task_name = task.replace("_", " ")
    #     print(f'<li><a href="{task}.html">{task_name}</a></li>')
    # exit()
    embodiments_dic = {
        'ALOHA': 'aloha-agilex',
        'X5': 'ARX-X5',
        'FRANKA': 'franka-panda',
        'PIPER': 'piper',
        'UR5': 'ur5-wsg'
    }
    task_ave_step = load_yml('./task_average_len.yml')
    task_objects_dic = load_json('./tasks_objects.json')
    html_tmp = '''<!DOCTYPE html>
<html lang="en">
<body>
    <div style="display: flex;">
        <video src="./task_video_clean/${TASK}$/aloha-agilex_head.mp4" controls loop muted autoplay style="width: 25%;"></video>
        <video src="./task_video_clean/${TASK}$/franka-panda_head.mp4" controls loop muted autoplay style="width: 25%;"></video>
        <video src="./task_video_clean/${TASK}$/ARX-X5_head.mp4" controls loop muted autoplay style="width: 25%;"></video>
        <video src="./task_video_clean/${TASK}$/piper_head.mp4" controls loop muted autoplay style="width: 25%;"></video>
        <video src="./task_video_clean/${TASK}$/ur5-wsg_head.mp4" controls loop muted autoplay style="width: 25%;"></video>
    </div>
    <div style="display: flex;">
        <video src="./task_video_clean/${TASK}$/aloha-agilex_world.mp4" controls loop muted autoplay style="width: 25%;"></video>
        <video src="./task_video_clean/${TASK}$/franka-panda_world.mp4" controls loop muted autoplay style="width: 25%;"></video>
        <video src="./task_video_clean/${TASK}$/ARX-X5_world.mp4" controls loop muted autoplay style="width: 25%;"></video>
        <video src="./task_video_clean/${TASK}$/piper_world.mp4" controls loop muted autoplay style="width: 25%;"></video>
        <video src="./task_video_clean/${TASK}$/ur5-wsg_world.mp4" controls loop muted autoplay style="width: 25%;"></video>
    </div>
    <br><b>Description</b>: ${TASK_DESCRIPTION}$<br>
    <b>Average Steps</b>: ${TASK_AVE_STEPS}$<br>
    <b>Objects</b>: ${TASK_USE_OBJ}$<br>
    <table style="margin:0 auto;border-collapse:collapse;width:auto;min-width:180px;background-color:white;">
        <thead>
            <tr style="background:#f0f0f0;">
                <th style="border:1px solid #ccc;padding:6px 14px;color:black;">Embodiments</th>
                <th style="border:1px solid #ccc;padding:6px 14px;color:black;">Aloha-AgileX</th>
                <th style="border:1px solid #ccc;padding:6px 14px;color:black;">ARX-X5</th>
                <th style="border:1px solid #ccc;padding:6px 14px;color:black;">Franka-Panda</th>
                <th style="border:1px solid #ccc;padding:6px 14px;color:black;">Piper</th>
                <th style="border:1px solid #ccc;padding:6px 14px;color:black;">UR5-Wsg</th>
            </tr>
        </thead>
        <tbody>
            <tr style="background:white;">
                <td style="border:1px solid #ccc;padding:6px 14px;color:black;">Success Rate</td>
                <td style="border:1px solid #ccc;padding:6px 14px;color:black;">${ALOHA}$</td>
                <td style="border:1px solid #ccc;padding:6px 14px;color:black;">${X5}$</td>
                <td style="border:1px solid #ccc;padding:6px 14px;color:black;">${FRANKA}$</td>
                <td style="border:1px solid #ccc;padding:6px 14px;color:black;">${PIPER}$</td>
                <td style="border:1px solid #ccc;padding:6px 14px;color:black;">${UR5}$</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
'''
    error_task_embodiment = []
    for task in task_list:
        task_name = task.replace("_", " ")
        # high_light = f'<li style="background:#e6f7e6;"><a href="{task}.html" style="font-weight:bold;">{task_name}</a></li>'
        # old_display = f'<li><a href="{task}.html">{task_name}</a></li>'
        description = load_json(f'./task_instruction/{task}.json')["full_description"]
        ave_step = task_ave_step[task]
        embodiments_success_rate = get_embodiments_success_rates(task)
        objects = ""
        for obj in task_objects_dic[task]:
            if objects != "":
                objects += ", "
            objects += obj
        success_num = 0
        for embodiment in embodiments_success_rate.keys():
            if (os.path.exists(f'./task_video_clean/{task}/{embodiments_dic[embodiment]}_head.mp4') )or (embodiments_success_rate[embodiment] > 0):
                success_num += 1
        video_width = 100 / success_num
        now_html_file = html_tmp
        # now_html_file = now_html_file.replace(old_display, high_light)
        now_html_file = now_html_file.replace("${TASK}$", task)
        now_html_file = now_html_file.replace("${TASK_NAME}$", task_name)
        now_html_file = now_html_file.replace("${TASK_AVE_STEPS}$", str(ave_step)+" (Aloha-AgileX, save_freq=15)")
        now_html_file = now_html_file.replace("${TASK_DESCRIPTION}$", description)
        now_html_file = now_html_file.replace("${TASK_USE_OBJ}$", objects)

        for embodiment in embodiments_success_rate.keys():
            now_html_file = now_html_file.replace("${"+embodiment.upper()+"}$", str(embodiments_success_rate[embodiment])+'%')
            if not os.path.exists(f'./task_video_clean/{task}/{embodiments_dic[embodiment]}_head.mp4'):
                if embodiments_success_rate[embodiment] > 0:
                    error_task_embodiment.append((task, embodiment, "No video"))
                video_path = f'./task_video_clean/{task}/{embodiments_dic[embodiment]}'
                now_html_file = now_html_file.replace(f'<video src="{video_path}_head.mp4" controls loop muted autoplay style="width: 25%;"></video>', '')
                now_html_file = now_html_file.replace(f'<video src="{video_path}_world.mp4" controls loop muted autoplay style="width: 25%;"></video>', '')
            else:
                if embodiments_success_rate[embodiment] == 0:
                    error_task_embodiment.append((task, embodiment, "0 success rate"))
                else :
                    video_path = f'./task_video_clean/{task}/{embodiments_dic[embodiment]}'
                    now_html_file = now_html_file.replace(f'<video src="{video_path}_head.mp4" controls loop muted autoplay style="width: 25%;"></video>', 
                                                          f'<video src="{video_path}_head.mp4" controls loop muted autoplay style="width: {video_width}%;"></video>')
                    now_html_file = now_html_file.replace(f'<video src="{video_path}_world.mp4" controls loop muted autoplay style="width: 25%;"></video>', 
                                                          f'<video src="{video_path}_world.mp4" controls loop muted autoplay style="width: {video_width}%;"></video>')
        save_html_file(f'./{task}.md', now_html_file)
    for item in error_task_embodiment:
        print(item)
