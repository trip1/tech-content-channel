# Block script: I found container-speed VMs for Proxmox. There is one catch.

## Format notes

- Target length: 8-11 minutes
- Style: technical, honest, story-first
- Delivery: curious but cautious. This is exciting, not magic.
- Editing rhythm: fast opening, then slow down when risk appears, then build momentum during the terminal sequence.

## Open loops to maintain

1. Does this actually boot like a container?
2. Is patching Proxmox a dealbreaker?
3. Where should this live in a real homelab: LXC, VM, or microVM?

---

## Block 1: cold open, show the prize and the danger

**Time:** 0:00-0:30

**On screen**

- Fast cuts:
  - Proxmox UI
  - terminal starting a microVM
  - serial console
  - quick diagram: LXC / VM / microVM
  - warning card: "PATCHES PROXMOX"

**Voiceover / talking head**

I found a Proxmox project that promises something I have wanted for a while: VMs that feel almost as quick as containers.

Not LXC. Actual KVM isolation. A real VM boundary. But with the startup behavior of something much smaller.

And then I saw the catch.

It patches Proxmox itself.

So in this video, I am going to test it the way I would actually test it in a homelab: check the host, install it carefully, build one tiny microVM, boot it, and then decide where this makes sense, and where it absolutely does not.

**Retention beat**

Cut on: "It patches Proxmox itself."

Hold a half-second pause. Let it feel risky.

---

## Block 2: the problem, the homelab tradeoff nobody likes

**Time:** 0:30-1:35

**On screen**

- Diagram: LXC on left, full VM on right
- LXC shares host kernel
- VM has its own kernel but boots full virtual hardware

**Voiceover / talking head**

If you run Proxmox long enough, you end up making this choice constantly.

LXC containers are fast. They start instantly, they barely use resources, and for trusted services they are great. I use them all the time.

But they share the host kernel. That is the part people forget when everything is working. If the workload is sketchy, experimental, or running code you do not fully trust, LXC is not the same kind of security boundary as a VM.

Full VMs solve that. You get KVM isolation, your own kernel, your own OS, and a much cleaner mental model.

But full VMs bring baggage. BIOS or UEFI, bootloaders, emulated devices, VGA, USB controllers, PCI bridges. All the little pieces that make a VM feel like a computer from 2009 waking up from a nap.

So the boring tradeoff has always been: fast and less isolated, or isolated and heavier.

This project is trying to split that tradeoff in half.

---

## Block 3: introduce pve-microvm

**Time:** 1:35-2:35

**On screen**

- GitHub repo: `rcarmo/pve-microvm`
- Article title: "Running microVMs in Proxmox VE, The Easy Way"
- Highlight package components:
  - `.deb`
  - custom kernel
  - template builder
  - Proxmox UI integration

**Voiceover / talking head**

The project is called `pve-microvm`, by Rui Carmo. The idea is to make QEMU's `microvm` machine type feel like a first class Proxmox guest.

A microVM strips the machine down to the parts a server workload actually needs. No BIOS. No GRUB. No VGA. No USB. Direct kernel boot, virtio disk, virtio networking, serial console.

That is why it can boot so quickly. You are not waiting for a tiny pretend PC to initialize. You are handing QEMU a kernel and a root filesystem and saying: go.

The package also includes tools to build root filesystems from OCI images, so instead of installing Debian from an ISO, you can build a tiny Debian or Alpine microVM template from a container image.

That is the cool part.

The uncomfortable part is how it integrates with Proxmox. It patches Proxmox's `qemu-server` Perl modules so that `machine: microvm` works inside the normal `qm` and web UI flow.

That is powerful. It is also exactly why we are not going to treat this like a random Docker compose file.

---

## Block 4: host fit check before installing anything

**Time:** 2:35-3:45

**On screen**

Run or show commands:

```bash
pveversion
apt-cache policy qemu-server pve-qemu-kvm
qemu-system-x86_64 -machine help | grep microvm
ls -l /dev/kvm
egrep -o 'svm|vmx' /proc/cpuinfo | sort -u
pvesm status
```

**Voiceover / talking head**

Before installing anything, I want to answer three questions.

First, is this host even compatible?

The project wants Proxmox VE 9, QEMU 10, and KVM. On my host, that checks out. Proxmox 9, QEMU has the `microvm` machine type, `/dev/kvm` exists, and the CPU has AMD virtualization support.

Second, do I have room to test safely?

This matters because microVMs still use Proxmox storage. They are smaller than normal VMs, but they are not free. On my box, `local-lvm` has been running tight, so I am going to keep this test tiny. If your Proxmox storage is already near full, fix that first.

Third, can I recover?

This is the boring question, but it is the most important one. If this is your only Proxmox host and you have no backups, stop here. Set up backups first. The package is reversible, but "reversible" is not the same thing as "I do not need backups."

**On-screen callout**

"Rule: experimental host changes happen after backups, not before."

---

## Block 5: install pve-microvm

**Time:** 3:45-5:00

**On screen**

Commands:

```bash
cd /root
curl -sLO "$(curl -s https://api.github.com/repos/rcarmo/pve-microvm/releases/latest \
  | grep browser_download_url \
  | grep '.deb' \
  | cut -d'"' -f4)"

dpkg -i pve-microvm_*.deb
apt-get install -f
/usr/share/pve-microvm/pve-microvm-patch status
```

**Voiceover / talking head**

Installation is surprisingly simple. It is a Debian package. Pull the latest release, install it with `dpkg`, then let apt fix any missing dependencies.

The important verification step is the patch status command.

I do not want to see "the package installed" and call it done. I want to see that the Proxmox patch is actually applied.

Because this is the part that makes the whole thing work. When a VM config says `machine: microvm`, Proxmox needs to hand that config off to the microVM command builder instead of building a normal QEMU PC.

If that patch is missing, you can get weird failures. The article calls out one especially nasty case: the disk can appear as `/dev/sda` instead of `/dev/vda`, and suddenly your guest looks like it lost its root filesystem even though the data is still there.

That is the kind of bug that makes a homelabber say words the YouTube algorithm does not like.

**Editing beat**

Show a quick redacted terminal success state. Do not linger.

---

## Block 6: create the template

**Time:** 5:00-6:25

**On screen**

Debian option:

```bash
pve-microvm-template \
  --image debian:trixie-slim \
  --vmid 9000 \
  --name microvm-debian-trixie \
  --storage local-lvm \
  --disk-size 2G \
  --memory 512 \
  --cores 1 \
  --profile standard
```

Alpine lighter option:

```bash
pve-microvm-template \
  --image alpine:3.21 \
  --vmid 9001 \
  --name microvm-alpine \
  --storage local-lvm \
  --disk-size 1G \
  --memory 256 \
  --cores 1 \
  --profile standard
```

**Voiceover / talking head**

This is where the workflow feels less like a normal VM and more like a container pipeline.

We are not booting an ISO. There is no installer screen. The template tool pulls an OCI image, builds a root filesystem, adds the bits needed for the microVM environment, and registers it as a Proxmox template.

For a first test, I would use Alpine if I only care about proving the concept, or Debian if I want something closer to a normal server environment.

I am keeping the disk small on purpose. The goal is not to build a production service yet. The goal is to prove that the host can create, clone, boot, and manage one of these cleanly.

**On-screen callout**

"First test: small disk, boring distro, DHCP, no heroics."

---

## Block 7: clone and boot the first microVM

**Time:** 6:25-7:45

**On screen**

Commands:

```bash
qm clone 9000 901 --name test-microvm --full
qm set 901 --machine microvm --memory 1024 --cores 2
qm start 901
qm terminal 901
```

Optional checks:

```bash
qm agent 901 ping
qm guest exec 901 -- ip addr
qm shutdown 901
qm start 901
```

**Voiceover / talking head**

Now we clone the template into a real VM.

This part is intentionally familiar. `qm clone`, `qm set`, `qm start`. The whole promise of the project is that microVMs still feel like Proxmox guests. Same storage. Same bridge networking. Same backup tools. Same mental model.

The difference is in the config.

You will see `machine: microvm`, serial console, and the kernel args pointing at the host-provided microVM kernel.

When it boots, do not expect a graphical console. There is no VGA here. The console is serial, so `qm terminal` is your friend.

And if this works, that is the moment the project becomes interesting. Because now you have a VM boundary that starts to feel much closer to a container.

**Editing beat**

If boot is visibly fast, show it in real time. If not, compress the wait but show the timing honestly.

---

## Block 8: what you gain

**Time:** 7:45-8:45

**On screen**

Decision matrix:

| Workload | LXC | microVM | full VM |
|---|---|---|---|
| trusted service | best | maybe | overkill |
| untrusted code | risky | good | good |
| Docker sandbox | messy sometimes | good | good |
| desktop / GUI | no | no | good |
| USB / GPU passthrough | maybe | no | good |

**Voiceover / talking head**

So what do we actually gain?

The biggest win is isolation for workloads that are a little too sketchy for LXC but do not deserve a full traditional VM.

AI coding agents. CI runners. Disposable sandboxes. Tiny reverse proxies. Mini firewalls. Anything where you want to snapshot it, clone it, boot it fast, and not share the host kernel.

It also makes Docker-in-a-guest feel cleaner than Docker-in-LXC. You are still inside a VM. You have a guest kernel. You are not negotiating with LXC nesting and overlay edge cases quite as much.

This is the category I find most compelling: semi-trusted automation. Stuff that is useful, but not something I want rubbing directly against the host kernel.

---

## Block 9: what can go wrong

**Time:** 8:45-9:55

**On screen**

Warning list:

- Experimental
- Patches Proxmox internals
- No VGA
- No USB
- No PCI/GPU passthrough
- No live migration
- Host-provided kernel
- Backups first

**Voiceover / talking head**

Now the part that keeps this from being an automatic recommendation.

This is experimental. It patches Proxmox internals. The author has done a lot of work to make the patches reversible and resilient across upgrades, but Proxmox was not designed around this as a native guest type.

That means I would not put this on a production cluster casually. I would not install it right before a trip. I would not install it on a host with no backups and then act surprised if a future Proxmox upgrade needs attention.

There are also real limitations.

No VGA. No desktop guests. No USB. No Zigbee dongle passthrough. No GPU passthrough today. No live migration. And Linux guests use the kernel shipped on the Proxmox host, which is part of why this is fast, but also part of why it is different.

None of that makes it bad.

It just means this is not a replacement for every VM or every LXC. It is a new slot in the toolbox.

---

## Block 10: when I would use it

**Time:** 9:55-10:50

**On screen**

Three cards:

1. Keep using LXC when you trust the workload
2. Use microVMs for fast isolated sandboxes
3. Use full VMs for hardware, GUI, or boring production stability

**Voiceover / talking head**

Here is where I land.

If the workload is trusted and simple, I am still using LXC. It is efficient, easy, and battle tested in Proxmox.

If the workload needs hardware passthrough, a normal installer, a GUI, USB, or boring production support, I am using a full VM.

But if I want a fast, isolated Linux box for experiments, agents, CI workers, sketchy scripts, or anything I want to clone and throw away, microVMs make a lot of sense.

The phrase I keep coming back to is: container workflow, VM boundary.

That is a pretty good thing to have in a homelab, as long as you respect the fact that the integration layer is still experimental.

---

## Block 11: close and next video tease

**Time:** 10:50-11:20

**On screen**

- Show the running test microVM
- Show Proxmox resource tree
- Tease network isolation diagram: VLAN / firewall / AI agent sandbox

**Voiceover / talking head**

So that is the setup. One package, one template, one cloned microVM, and a very clear warning label.

I do not think this replaces LXC. I do not think it replaces full VMs. I think it fills the awkward gap between them.

And that gap is exactly where a lot of modern homelab experiments live.

If you want the follow-up, I will take one of these microVMs and turn it into a properly isolated AI/code-agent sandbox on its own network segment, with Proxmox firewall rules and a disposable workflow.

Comment `microVM` if you want that build next.

---

# Pinned comment draft

The project is `rcarmo/pve-microvm`. It is experimental and patches Proxmox internals, so back up your host first and test on non-critical infrastructure. If your `local-lvm` is tight, create a tiny test template or use separate test storage.

Commands and notes from the video are in the description.

# Description draft

I tested `pve-microvm`, a Proxmox VE project that adds QEMU microVM support so you can run tiny hardware-isolated VMs with container-like startup times.

In this video:

- Why LXC vs full VM is an annoying homelab tradeoff
- What QEMU microVMs are
- How `pve-microvm` integrates with Proxmox
- The safety checks I would run first
- Installing the package
- Creating a Debian or Alpine microVM template
- Cloning and booting a test microVM
- Where microVMs make sense, and where they do not

Important: this is experimental and patches Proxmox's `qemu-server` internals. Do not install it on a critical host without backups.

Project: https://github.com/rcarmo/pve-microvm
Article: https://taoofmac.com/space/blog/2026/06/18/1845

# Chapters draft

00:00 The promise and the catch
00:30 LXC vs full VMs
01:35 What pve-microvm does
02:35 Host safety checks
03:45 Installing the package
05:00 Creating a microVM template
06:25 Cloning and booting
07:45 What you gain
08:45 What can go wrong
09:55 When I would use microVMs
10:50 Next build

# Shorts cut ideas

1. **"VMs that boot like containers?"**
   - 20-30 seconds
   - Hook: "This Proxmox package gives you the one thing I wanted: VM isolation without full VM boot baggage."
   - End: "The catch? It patches Proxmox itself."

2. **"LXC vs microVM in one minute"**
   - Show shared kernel vs KVM boundary
   - End with decision rule

3. **"The scary command in this Proxmox setup"**
   - Focus on patch status and why it matters
   - Good curiosity clip
