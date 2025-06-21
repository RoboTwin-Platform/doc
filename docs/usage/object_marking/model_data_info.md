**center**: 物体中心，相对于物体资产坐标的偏移向量（x y z）: 1\*3 matrix
**extents**: 资产长宽高（x y z 坐标轴上的长度）: 1\*3 matrix
**scale**: 场景中对实际物体资产的缩放（x y z方向上）: 1\*3 matrix
**target_pose**: 已被废除，无含义，一般不标定
**contact_points_pose**: list列表，列表元素为4\*4旋转+平移矩阵，表示抓取点与物体中心坐标的偏移: n\*4\*4 matrix
**transform_matrix**: 不重要，一般不标定
**functional_matrix**: list列表，列表元素为4\*4旋转+平移矩阵，表示功能点与物体中心坐标的偏移: n\*4\*4 matrix
**orientation_point**: 方向点，一般不标定
**contact_points_group**: 抓取点分组，原因为有些抓取点xyz坐标相同，但是轴的方向不同，我们把这部分抓取点分到同个group内，方便一些操作
**contact_points_mask**: 自动生成，无需标定（似乎被废除了）
**contact_points_discription**: 抓取点描述: 1\*n str
**functional_point_discription**: 功能点描述: 1\*n str
**orientation_point_discription**： 方向点描述: 1\*n str

**注意**：描述标定一般通过直接更改json文件来标定，不是强格式标定数据，也可通过其他表示方法外部标定。