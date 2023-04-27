

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("746x661")
window.configure(bg = "#FFFFFF")

username = StringVar()
password = StringVar()

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 661,
    width = 746,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    112.0,
    73.0,
    634.6497802734375,
    614.183349609375,
    fill="#BAB8B8",
    outline="")

# canvas.create_text(
#     411.0,
#     545.0,
#     anchor="nw",
#     text="Register here",