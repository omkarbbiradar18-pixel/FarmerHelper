#Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
#Enter "help" below or click "Help" above for more information.
#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk, messagebox

def normalize(s):
    return (s or "").strip().lower()

def generate_advice(soil_type, crop, season):
    s = normalize(soil_type)
    c = normalize(crop)
    se = normalize(season)

    if s in ("sandy", "sandy loam"):
        watering = "Frequent light watering — sandy soils drain fast."
    elif s in ("clay", "heavy clay"):
        watering = "Less frequent, deep watering — clay holds water, avoid waterlogging."
    elif s in ("loamy", "loam"):
        watering = "Moderate watering — loam holds moisture well."
    else:
        watering = "Adjust watering based on soil texture."

    if c == "rice":
        fertilizer = "Use N-P-K; split nitrogen at tillering and panicle initiation."
    elif c == "wheat":
        fertilizer = "Apply P & K at base; split nitrogen at tillering."
    elif c in ("maize", "corn"):
        fertilizer = "High nitrogen needed — apply at planting & knee-high stage."
    elif c in ("tomato", "potato"):
        fertilizer = "Balanced NPK; extra potassium during fruit/tuber growth."
    else:
        fertilizer = "Use balanced N-P-K based on soil test."

    pests = "Check pests regularly; follow crop rotation and field cleaning."
    if se in ("monsoon", "kharif"):
        pests += " Wet season increases fungal diseases."
    if se == "summer":
        pests += " Heat increases borers and sucking pests."
    if c in ("tomato", "potato"):
        pests += " Watch for blight & aphids."

    tips = "Do a soil test; maintain organic matter."
    if s == "clay":
        tips += " Improve drainage, add compost."
    if s == "sandy":
        tips += " Add compost to retain moisture."
    if se in ("kharif", "monsoon"):
        tips += " Use disease-tolerant varieties."

    return {
        "Watering": watering,
        "Fertilizer": fertilizer,
        "Pests": pests,
        "Tips": tips,
    }

class AgriApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Agriculture Helper")
        self.geometry("520x360")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Soil Type:").grid(row=0, column=0, sticky=tk.W)
        self.soil = tk.StringVar()
        ttk.Entry(frame, textvariable=self.soil, width=30).grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Crop:").grid(row=1, column=0, sticky=tk.W)
        self.crop = tk.StringVar()
        ttk.Entry(frame, textvariable=self.crop, width=30).grid(row=1, column=1, pady=5)

        ttk.Label(frame, text="Season:").grid(row=2, column=0, sticky=tk.W)
        self.season = tk.StringVar()
        ttk.Entry(frame, textvariable=self.season, width=30).grid(row=2, column=1, pady=5)

        ttk.Button(frame, text="Generate Advice", command=self.generate).grid(
            row=3, column=0, columnspan=2, pady=10
        )

        self.output = tk.Text(frame, height=8, wrap=tk.WORD)
        self.output.grid(row=4, column=0, columnspan=2, sticky="nsew")
        frame.rowconfigure(4, weight=1)

    def generate(self):
        soil = self.soil.get()
        crop = self.crop.get()
        season = self.season.get()

        if not soil or not crop or not season:
            messagebox.showwarning("Missing Data", "Please fill all fields!")
            return

        advice = generate_advice(soil, crop, season)

        text = (
            f"- Watering: {advice['Watering']}\n"
            f"- Fertilizer: {advice['Fertilizer']}\n"
            f"- Pests: {advice['Pests']}\n"
            f"- Tips: {advice['Tips']}"
        )

        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, text)

if __name__ == "__main__":
    app = AgriApp()
    app.mainloop()
