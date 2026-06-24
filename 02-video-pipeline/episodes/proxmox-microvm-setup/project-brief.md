# Video project: Container-speed VMs in Proxmox

## Working title

**I found container-speed VMs for Proxmox. There is one catch.**

## Core promise

Show viewers how to set up `pve-microvm` on Proxmox so they can run tiny, fast, hardware-isolated microVMs from OCI images, while being honest about the risk: it patches Proxmox internals and should be tested carefully.

## Audience

Homelab / Proxmox / Linux viewers who currently choose between:

- LXC: fast and efficient, but shared kernel
- full VM: safer isolation, but heavier and slower
- Docker-in-LXC: works, but can get weird with overlayfs, nesting, cgroups, and permissions

## Viewer transformation

Before: "I know LXC and VMs, but I don't know where microVMs fit."

After: "I understand what `pve-microvm` gives me, when I should use it, when I should not, and the safe path to test it on my own Proxmox box."

## Story angle

This is not a normal setup tutorial. It is a tension story:

> Homelabbers have been stuck with a bad tradeoff: containers are fast but share the host kernel; VMs are isolated but feel heavy. Then a small experimental Proxmox package shows up promising the middle path. It works like a VM, boots like a container, and installs from a single `.deb`. But the catch is serious: it patches Proxmox itself.

## Paddy Galloway-inspired packaging notes

Sources checked:

- Colin & Samir recap of Paddy Galloway: YouTube is a "click & watch" platform; spend more time on ideation and packaging; be familiar but unexpected; borrow proven formats across niches; small packaging tweaks can create huge performance swings.
- Marketing Examined summary: titles should be short, clear, emotionally resonant; thumbnails should complement the title and tease the story; open straight into storyline; set stakes early; use CTR and average view duration together.

How this video applies that:

| Paddy-style principle | Video decision |
|---|---|
| Click + watch, not just information | Title has curiosity plus a clear niche: "container-speed VMs for Proxmox" + "one catch" |
| Familiar but unexpected | Familiar tutorial format, unexpected premise: a third option between LXC and VMs |
| Set stakes early | Host Proxmox risk: this patches `qemu-server`; do not install casually |
| Respect viewer time | Show the end result in the first 20 seconds before explaining theory |
| Borrow proven formats | "I tested the tool everyone will ask about" + "works, but here's the catch" |
| Retention through open loops | Keep three loops alive: Will it boot? Is it safe? Should you use it instead of LXC? |

## Title ideas

1. **I found container-speed VMs for Proxmox. There is one catch.**
2. **This Proxmox trick boots VMs like containers**
3. **Proxmox microVMs: safer than LXC, faster than full VMs?**
4. **I tested microVMs in Proxmox so you don't break your server**
5. **The weird Proxmox feature I wish was built in**

Best pick: **I found container-speed VMs for Proxmox. There is one catch.**

Reason: clear audience, curiosity gap, stakes, not too technical for the title.

## Thumbnail concepts

### Concept A: tradeoff triangle

Visual:

- Left: LXC box labeled "FAST"
- Right: VM box labeled "SAFE"
- Middle: glowing tiny VM labeled "microVM"
- Red warning tape: "PATCHES PROXMOX"

Thumbnail text: **FAST VMs?**

### Concept B: Proxmox UI shock

Visual:

- Proxmox dashboard screenshot blurred/darkened
- Big amber lightning bolt icon over a VM
- Small red label: "EXPERIMENTAL"

Thumbnail text: **µVMs in Proxmox**

### Concept C: speed test

Visual:

- Stopwatch at 0.3s
- VM icon launching
- Container icon beside it

Thumbnail text: **0.3s VM BOOT**

## Target length

8-11 minutes.

## Cadence plan

| Time | Purpose | Retention job |
|---:|---|---|
| 0:00-0:25 | Cold open: show the result and the catch | Immediate payoff + risk loop |
| 0:25-1:20 | The LXC vs VM tradeoff | Make the pain familiar |
| 1:20-2:20 | What `pve-microvm` is | Introduce the third option |
| 2:20-3:15 | Host safety check | Stakes: should you install this? |
| 3:15-5:30 | Install + verify package | Practical tutorial momentum |
| 5:30-7:15 | Create template + clone test VM | Main build payoff |
| 7:15-8:45 | What works / what doesn't | Decision clarity |
| 8:45-10:00 | Should you use it? | Honest recommendation |
| 10:00-10:30 | Wrap + next video tease | Comment prompt + series hook |

## Required screen recordings

- Proxmox dashboard before install
- Terminal: `pveversion`, `qemu-system-x86_64 -machine help | grep microvm`, `/dev/kvm`
- GitHub release page for `rcarmo/pve-microvm`
- Install commands
- Patch status command
- Create template command
- Clone + boot command
- `qm terminal <vmid>` showing serial console
- Optional: quick boot timing shot
- Rollback/uninstall command shown on screen, not necessarily executed

## Required b-roll / graphics

- Simple diagram: LXC vs VM vs microVM
- Warning card: "Experimental: patches Proxmox internals"
- Decision matrix: use LXC / use microVM / use full VM
- Animated boot sequence: firmware/GRUB skipped

## Technical notes from our Proxmox check

Your host is a good candidate for a cautious test:

- Proxmox VE 9.1.7
- `qemu-server` 9.1.6
- `pve-qemu-kvm` 10.1.2-7
- QEMU reports `microvm` machine support
- `/dev/kvm` exists
- AMD virtualization flag `svm` exists

Main caveat for filming/setup:

- `local-lvm` was around 92% full in the prior health check. Do not create lots of templates/clones there without cleanup. For the video, either free space first or use a tiny 1-2GB test template.

## Key claims to verify during recording

- Latest release version at recording time
- Install succeeds
- `/usr/share/pve-microvm/pve-microvm-patch status` says applied
- A template can be created
- A cloned microVM boots
- Console works over serial
- Network works via DHCP
- Guest agent responds, if using the standard profile

## Risk disclaimer to say on camera

"Do not install this on your only production Proxmox host without backups. This is experimental, and the entire trick works by patching Proxmox's `qemu-server` internals. That does not make it bad, but it does mean you treat it differently from a normal apt package."

## Recommended CTA

"If you want the follow-up, I'll do the unsafe thing safely: isolate one of these microVMs on its own VLAN and use it as an AI/code-agent sandbox. Comment `microVM` if you want that build." 
