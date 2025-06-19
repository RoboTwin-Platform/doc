import os

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

if __name__ == "__main__":
    obj_list = [
        '001_bottle', 
        '002_bowl', 
        '003_plate', 
        '004_fluted-block', 
        '005_french-fries', 
        '006_hamburg', 
        '007_shoe-box', 
        '008_tray', 
        '009_kettle', 
        '010_pen', 
        '011_dustbin', 
        '012_plant-pot', 
        '013_dumbbell-rack', 
        '014_bookcase', 
        '015_laptop', 
        '016_oven', 
        '017_calculator', 
        '018_microphone', 
        '019_coaster', 
        '020_hammer', 
        '021_cup', 
        '022_cup-with-liquid', 
        '023_tissue-box', 
        '024_scanner', 
        '025_chips-tub', 
        '026_pet-collar', 
        '027_table-tennis', 
        '028_roll-paper', 
        '029_olive-oil', 
        '030_drill', 
        '031_jam-jar', 
        '032_screwdriver', 
        '033_fork', 
        '034_knife', 
        '035_apple', 
        '036_cabinet', 
        '037_box', 
        '038_milk-box', 
        '039_mug', 
        '040_rack', 
        '041_shoe', 
        '042_wooden_box', 
        '043_book', 
        '044_microwave', 
        '045_sand-clock', 
        '046_alarm-clock', 
        '047_mouse', 
        '048_stapler', 
        '049_shampoo', 
        '050_bell', 
        '051_candlestick', 
        '052_dumbbell', 
        '053_teanet', 
        '054_baguette', 
        '055_small-speaker', 
        '056_switch', 
        '057_toycar', 
        '058_markpen', 
        '059_pencup', 
        '060_kitchenpot', 
        '061_battery', 
        '062_plasticbox', 
        '063_tabletrashbin', 
        '064_msg', 
        '065_soy-sauce', 
        '066_vinegar', 
        '067_steamer', 
        '068_boxdrink', 
        '069_vagetable', 
        '070_paymentsign', 
        '071_can', 
        '072_electronicscale', 
        '073_rubikscube', 
        '074_displaystand', 
        '075_bread', 
        '076_breadbasket', 
        '077_phone', 
        '078_phonestand', 
        '079_remotecontrol', 
        '080_pillbottle', 
        '081_playingcards', 
        '082_smallshovel', 
        '083_brush', 
        '084_woodenmallet', 
        '085_gong', 
        '086_woodenblock', 
        '087_waterer', 
        '088_wineglass', 
        '089_globe', 
        '090_trophy', 
        '091_kettle', 
        '092_notebook', 
        '093_brush-pen', 
        '094_rest', 
        '095_glue', 
        '096_cleaner', 
        '097_screen', 
        '098_speaker', 
        '099_fan', 
        '100_seal', 
        '101_milk-tea', 
        '102_roller', 
        '103_fruit', 
        '104_board', 
        '105_sauce-can', 
        '106_skillet', 
        '107_soap', 
        '108_block', 
        '109_hydrating-oil', 
        '110_basket', 
        '111_callbell', 
        '112_tea-box', 
        '113_coffee-box', 
        '114_bottle', 
        '115_perfume', 
        '116_keyboard', 
        '117_whiteboard-eraser', 
        '118_tooth-paste', 
        '119_mini-chalkboard', 
        '120_plant'
    ]

    obj_head_data = '''<!DOCTYPE html>
<html lang="en">
<body>
    <div class="layout">
        <div class="container">
    '''
    show_code = '''             <div style="flex: 0 0 auto; text-align: center;">
                <img src="./objects_imgs/${OBJ_NAME}$/base{ID}.jpg" 
                    alt="base{ID}" 
                    style="width:100%; max-width:350px; border-radius:8px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
                <p style="margin-top:8px; font-size:16px; color:#555;">base{ID}</p>
            </div>
    '''
    obj_end_data = '''  <div class="content">
</body>
</html>
'''
    obj_error = []
    for obj in obj_list:
        # high_light = f'<li style="background:#e6f7e6;"><a href="{obj}.html" style="font-weight:bold;">{obj}</a></li>'
        # old_display = f'<li><a href="{obj}.html">{obj}</a></li>'
        now_html = obj_head_data
        # now_html += f'            <div class="title" style="font-size:32px;font-weight:900;">{obj}</div>\n'
        now_html += '            <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px;">\n'
        obj_png_dir = f'./objects_imgs/{obj}/'
        if not os.path.exists(obj_png_dir):
            print(f"Directory {obj_png_dir} does not exist. Skipping {obj}.")
            obj_error.append(obj)
            continue
        # obj_png_dir = '.'+obj_png_dir
        obj_png_files = os.listdir(obj_png_dir)
        obj_png_files = sorted([f for f in obj_png_files if f.endswith('.jpg')], key=lambda x: int(x[4:-4]))
        for base_id in range(len(obj_png_files)):
            if base_id > 0 and base_id%2 == 0:
                now_html += '            </div>\n            <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px;">\n'
            id = int(obj_png_files[base_id][4:-4])
            now_html += show_code.replace('${OBJ_NAME}$', obj).replace('{ID}', f'{id}')
        now_html += '           </div>\n'
        now_html += obj_end_data
        save_html_file(f'./{obj}.md', now_html)
    print(obj_error)