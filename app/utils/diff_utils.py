def truncate_diff(diff: str, max_chars: int = 12000) -> str:
    
    if len(diff) <= max_chars:
        return diff
    return diff[:max_chars] + "\n\n... [truncated for analysis] ..."
