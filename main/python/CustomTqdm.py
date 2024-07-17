from tqdm import tqdm
import time

class CustomTqdm(tqdm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def format_meter(self, n, total, elapsed, ncols=None, prefix='', ascii=False, unit='it', unit_scale=False, rate=None, bar_format=None, postfix=None, unit_divisor=1000.0, **extra_kwargs):
        # ANSI 颜色转义代码
        PURPLE = '\033[95m'
        GREEN = '\033[92m'
        ORANGE = '\033[93m'
        CYAN = '\033[96m'
        RED = '\033[91m'
        RESET = '\033[0m'
        
        # 计算百分比
        percentage = n / total
        percent = f"{percentage:.0%}"
        
        # 计算填充长度和剩余长度
        ncols = ncols or 50  # 如果 ncols 为空，默认为 50
        filled_length = int(percentage * (ncols - 2))
        remaining_length = ncols - filled_length - 2
        
        # 自定义模式：# 和 1-9
        number = str((n % 9) + 1)
        bar = "#" * filled_length + number
        if n < total:  # 只在未完成时添加剩余的 '━'
            bar += '━' * remaining_length
        
        # 时间格式
        elapsed_str = self.format_interval(elapsed)
        remaining_str = self.format_interval((total - n) / (n / elapsed)) if n > 0 else "0:00:00"
        
        total_str = f"{total:,}"
        n_str = f"{n:,}"
        
        # 计算速率
        rate_str = f"{n / elapsed:.2f} slide/s" if elapsed > 0 else "0 slide/s"
        
        # 将输出结果彩色化
        percent_colored = f"{PURPLE}{percent}{RESET}"
        n_str_colored = f"{GREEN}{n_str}{RESET}"
        total_str_colored = f"{GREEN}{total_str}{RESET}"
        elapsed_str_colored = f"{ORANGE}{elapsed_str}{RESET}"
        remaining_str_colored = f"{CYAN}{remaining_str}{RESET}"
        rate_str_colored = f"{RED}{rate_str}{RESET}"
        
        return f'{prefix} {percent_colored} {bar} {n_str_colored}/{total_str_colored}  [ {elapsed_str_colored} < {remaining_str_colored} , {rate_str_colored} ]'

# 使用自定义的 tqdm 进度条
for i in CustomTqdm(range(100025), desc="Custom Progress", ncols=50, leave=True):
    time.sleep(0.00001)
input("请按任意键退出...")