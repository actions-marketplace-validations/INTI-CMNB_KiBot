import pcbnew
for la in range(60):
    print(f"{pcbnew.BOARD.GetStandardLayerName(la)} ({la})")
