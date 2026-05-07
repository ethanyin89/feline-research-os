# Raw Images

This directory holds local image assets that belong to ingested source cards.

Use it for:

- paper figures
- supplementary figures
- pathology or histology panels
- radiograph or ultrasound example images
- tables exported as images only when no text-native version exists

Do not use it for:

- screenshots of the vault UI
- generated charts from outputs/
- decorative assets

## Layout

Store assets under disease buckets when possible:

- `raw/images/ckd/`
- `raw/images/fip/`
- `raw/images/hcm/`
- `raw/images/ibd/`
- `raw/images/diabetes/`
- `raw/images/shared/`

Recommended naming:

- `src-ckd-001-mechanism-schematic.jpg`
- `src-fip-019-outcome-treatment-protocol-summary-table.png`
- `src-hcm-020-pathology-histopathology-panel.png`

## Source Card Linkage

Every image stored here should be referenced from the matching source card:

```yaml
links:
  local_assets:
    - raw/images/ckd/src-ckd-001-mechanism-schematic.jpg
```

If a source should have images but they are not downloaded yet, keep `local_assets: []`
and add an `Image Asset TODO` section in the source card.

## Minimal Rule

If a figure changes interpretation of mechanism, recognition, endpoint, model, or
regulatory fit, it should not stay outside the vault.
