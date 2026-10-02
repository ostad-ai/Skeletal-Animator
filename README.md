🦴 Skeletal Animator (v0.1)

A professional, offline 2D cutout animation tool for animators and game developers. Build flexible bone skeletons, attach sprites or primitive shapes, and bring your characters to life using an intuitive timeline, FABRIK Inverse Kinematics, and cinematic camera keyframing.

Whether you are rigging a character for an indie game or creating a smooth 2D animation, Skeletal Animator provides a complete studio environment. Export your work as standard spritesheets (PNG+JSON) for your game engine, or render high-quality videos (MP4, WebM, GIF) with transparent background support!

This is the v0.1 release of the Skeletal Animator

---
<table>
<tr>
<td><img src="./Media/ver-0-0.jpg" alt="A snapshot of the Skeletal Animator, version 0.0" width="400">Figure 1. A snapshot of the Skeletal Animator, version 0.0
</td>
<td><img src="./Media/ver-0-0.jpg" alt="A snapshot of the Skeletal Animator, version 0.1" width="400">Figure 2. A snapshot of the Skeletal Animator, version 0.1
</td>
</tr>
</table>


---


## 📥 Download the App (Windows)

The main application is provided as a standalone Windows executable (for Windows 10 and over). You don't need Python installed to use it!

**[⬇️ Download skeletal_animator.exe](https://github.com/ostad-ai/Skeletal-Animator/releases/tag/v0.1)**

1. Download the `.exe` file.
2. Double-click to run.
3. Start animating immediately!

---

## 🆕 What's New in v0.1?

- **Pos-Only Link:** A new dropdown option in the toolbar. Link bones by position only, keeping their rotation independent. Perfect for torches, guns, or floating UI elements that shouldn't rotate with the hand!
- **Grid Toggle:** Press `Ctrl+G` (or use the View menu) to instantly show or hide the canvas grid.
- **Camera Controls:** Precise `Cam X/Y/W/H` spinboxes added to the toolbar for exact camera positioning.
- **Smooth Zoom:** High-precision zoom that feels buttery smooth on trackpads and mice.
- **Bug Fixes:** Fixed bone orientation loss when parenting, fixed timeline range syncing, and various UI polish improvements.

---

## ✨ Features

- **Rigging & IK:** Create bone chains, parent them with attachment offsets, and use Inverse Kinematics to automatically bend limbs naturally.
- **Skinning:** Import PNG sprites or generate primitive shapes (Rectangle, Capsule, Circle) with custom colors and non-uniform scaling.
- **Animation Studio:** A professional timeline with Keyframes, Easing (Linear, Ease In, Out, In-Out), and Onion Skinning (adjustable past/future ghosts).
- **Camera & Visibility:** Keyframe a camera viewport (Clip Window) to pan and zoom across your animation. Set visibility ranges so bones only appear on specific frames.
- **Workflow:** Z-Index for draw order, bone naming, copy/paste/cut for both bones and keyframes, and full Undo/Redo history.
- **Export:**
  - **Spritesheet:** Export a PNG grid + metadata JSON for your game engine.
  - **Video:** Export as MP4, WebM, MOV, or GIF. Supports transparent backgrounds for game engines!

---

## 💻 For Developers: Python Demo

To use the exported spritesheets in your own Python games, a demo script is provided in this repository.

### `demo_spritesheet.py`
A fully runnable Pygame demo that automatically reads the exported metadata JSON and plays the spritesheet animation smoothly.
* **To run:** 
  1. `pip install pygame`
  2. Export a track as `animation.png` and `animation.json` from the main app.
  3. Run `python demo_spritesheet.py`.
* **Controls:** `ESC` to Exit.

---

🌟 Support

If Skeletal Animator helps you bring your characters to life, please consider supporting us by giving this repository a ⭐ on GitHub! It helps other animators and developers discover the tool and fuels our future updates (and our virtual chai ☕)

---

## ❤️ Credits

Developed by Hamed Shah-Hosseini, under the V star (with lots of virtual chai). ☕

Built with Math, and a passion for animation and game development.

---
