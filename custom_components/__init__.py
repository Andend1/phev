import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

# Definer logger for integrasjonen
_LOGGER = logging.getLogger(__name__)

# Domenenavn for integrasjonen (brukes i manifest.json)
DOMAIN = "phev"

# Funksjon som kalles når Home Assistant starter integrasjonen
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the PHEV integration."""
    _LOGGER.info("Setting up the PHEV integration")
    
    # Du kan her legge til logikk for å initialisere tilkoblingen til bilen eller MQTT
    
    # For eksempel, hvis du har et sett med konfigurasjoner:
    hass.data[DOMAIN] = {}

    return True

# Funksjon som kalles når integrasjonen lastes inn via en config entry (for eksempel fra UI-oppsett)
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up PHEV from a config entry."""
    _LOGGER.info("Setting up PHEV from config entry")

    # Hent eventuelle lagrede konfigurasjoner fra oppsettet
    hass.data[DOMAIN] = entry.data

    # Her kan du starte tilkoblinger, lytte til hendelser osv.
    # For eksempel, start MQTT-kommunikasjon med bilen:
    # mqtt_client = await connect_to_phev(entry.data)

    return True

# Funksjon som kalles når en config entry fjernes (ved avinstallasjon eller lignende)
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    _LOGGER.info("Unloading PHEV config entry")

    # Her kan du stoppe tilkoblinger eller rydde opp når integrasjonen fjernes
    if DOMAIN in hass.data:
        hass.data.pop(DOMAIN)

    return True
