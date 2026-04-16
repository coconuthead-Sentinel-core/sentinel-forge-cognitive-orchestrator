class CognitiveWeatherMap {
    constructor(containerId) {
        this.container = document.getElementById(containerId);
        this.currentZone = 'GREEN'; // GREEN, YELLOW, RED
    }

    update(entropy) {
        let zone = 'GREEN';
        let weather = '✨ Clear Sky';
        let description = 'Flow State Active';
        let icon = '🌌';

        if (entropy > 0.4 && entropy <= 0.7) {
            zone = 'YELLOW';
            weather = '🌫️ Fog';
            description = 'Ambiguity Detected';
            icon = '🌫️';
        } else if (entropy > 0.7) {
            zone = 'RED';
            weather = '⛈️ Storm Front';
            description = 'Information Overload';
            icon = '⛈️';
        }

        this.currentZone = zone;
        this.render(zone, weather, description, icon, entropy);
    }

    render(zone, weather, description, icon, entropy) {
        if (!this.container) return;

        const colorMap = {
            'GREEN': '#10b981',
            'YELLOW': '#f59e0b',
            'RED': '#ef4444'
        };

        this.container.innerHTML = `
            <div style="text-align: center; padding: 20px; border: 2px solid ${colorMap[zone]}; border-radius: 10px; background: rgba(0,0,0,0.2);">
                <div style="font-size: 4em; margin-bottom: 10px;">${icon}</div>
                <h3 style="color: ${colorMap[zone]}; margin-bottom: 5px;">${weather}</h3>
                <p style="font-size: 0.9em; opacity: 0.8;">${description}</p>
                <div style="margin-top: 15px; background: rgba(255,255,255,0.1); height: 10px; border-radius: 5px; overflow: hidden;">
                    <div style="width: ${entropy * 100}%; height: 100%; background: ${colorMap[zone]}; transition: width 0.5s ease;"></div>
                </div>
                <div style="font-size: 0.8em; margin-top: 5px;">Entropy: ${entropy.toFixed(2)}</div>
            </div>
        `;
    }
}

window.CognitiveWeatherMap = CognitiveWeatherMap;
