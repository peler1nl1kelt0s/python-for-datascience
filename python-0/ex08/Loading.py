import sys
import time

def ft_tqdm(lst: range) -> None:
    """
        
    """
    total = len(lst)
    start_time = time.time()
    
    for i, item in enumerate(lst, 1):
        elapsed_time = time.time() - start_time
        rate = i / elapsed_time if elapsed_time > 0 else 0
        
        percent = i / total
        bar_length = 70
        filled_length = int(bar_length * percent)
        bar = '█' * filled_length + ' ' * (bar_length - filled_length)
        
        sys.stdout.write(f'\r{percent:3.0%}|{bar}| {i}/{total} [{elapsed_time:.2f}<{(total-i)/rate:.2f}, {rate:.2f}it/s]')
        sys.stdout.flush()
        
        yield item
    
    sys.stdout.write('\n')
    sys.stdout.flush()