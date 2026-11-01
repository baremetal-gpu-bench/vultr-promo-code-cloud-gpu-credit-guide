#!/usr/bin/env python3
"""Vultr Cloud GPU & Promo Credit TCO Calculator 2026."""
import argparse

GPU_HOURLY = {
    "a100_80gb": {"hourly": 2.60, "vram_gb": 80, "name": "NVIDIA A100 PCIe 80GB"},
    "a40": {"hourly": 1.25, "vram_gb": 48, "name": "NVIDIA A40 48GB"},
    "l40s": {"hourly": 1.95, "vram_gb": 48, "name": "NVIDIA L40S 48GB"},
    "gh200": {"hourly": 4.50, "vram_gb": 96, "name": "NVIDIA GH200 Grace Hopper"}
}

def calculate(gpu_sku="a100_80gb", running_hours=200, promo_credit=250):
    data = GPU_HOURLY.get(gpu_sku.lower(), GPU_HOURLY["a100_80gb"])
    gross_compute_cost = running_hours * data["hourly"]
    credit_applied = min(gross_compute_cost, promo_credit)
    net_outlay = gross_compute_cost - credit_applied
    remaining_credit = max(0, promo_credit - gross_compute_cost)

    print("=" * 65)
    print(f"Vultr Cloud GPU TCO & Free Credit Model: {data['name']}")
    print("=" * 65)
    print(f"Hourly On-Demand Rate:     ${data['hourly']:.2f} / hour")
    print(f"Monthly Workload Duration: {running_hours} hours")
    print(f"Gross Compute Charges:     ${gross_compute_cost:.2f}")
    print(f"Promotional Credit Credit: -${credit_applied:.2f} (from ${promo_credit} promo)")
    print(f"Net Out-of-Pocket Outlay:  ${net_outlay:.2f}")
    print(f"Remaining Free Credits:    ${remaining_credit:.2f}")
    print("=" * 65)
    return net_outlay, gross_compute_cost

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Vultr GPU Calculator")
    parser.add_argument("--gpu", default="a100_80gb", choices=["a100_80gb", "a40", "l40s", "gh200"])
    parser.add_argument("--hours", type=int, default=200)
    parser.add_argument("--credit", type=int, default=250)
    args = parser.parse_args()
    calculate(gpu_sku=args.gpu, running_hours=args.hours, promo_credit=args.credit)
