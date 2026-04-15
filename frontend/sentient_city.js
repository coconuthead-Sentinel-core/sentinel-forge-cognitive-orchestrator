class SentientCityDashboard {
    constructor(containerId) {
        this.container = document.getElementById(containerId);
        this.modules = {};
        this.init();
    }

    async init() {
        this.container.innerHTML = '<div style="text-align:center; padding: 20px;">Igniting Recursive Becoming...</div>';
        await this.fetchStatus();
        this.render();

        // Auto-refresh every 5 seconds
        setInterval(() => this.fetchStatus(), 5000);
    }

    async fetchStatus() {
        try {
            const response = await fetch('/api/city/status');
            this.modules = await response.json();
            this.render();
        } catch (e) {
            console.error("Failed to fetch city status:", e);
        }
    }

    render() {
        if (!this.container) return;

        let html = `
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; padding: 20px;">
        `;

        for (const [key, module] of Object.entries(this.modules)) {
            html += `
                <div class="city-module" style="
                    background: rgba(255, 255, 255, 0.1);
                    border-radius: 15px;
                    padding: 20px;
                    backdrop-filter: blur(10px);
                    border: 1px solid ${module.color};
                    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                    transition: transform 0.3s ease;
                " onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                    <div style="font-size: 3em; text-align: center; margin-bottom: 10px;">${module.icon}</div>
                    <h3 style="color: ${module.color}; text-align: center; margin-bottom: 5px;">${module.name}</h3>
                    <div style="text-align: center; font-size: 0.9em; opacity: 0.8; margin-bottom: 15px;">${module.role}</div>
                    
                    <div style="background: rgba(0,0,0,0.2); padding: 10px; border-radius: 8px; font-size: 0.85em;">
                        <div><strong>Function:</strong> ${module.function}</div>
                        <div style="margin-top: 5px; display: flex; align-items: center; justify-content: center;">
                            <span style="
                                display: inline-block;
                                width: 8px;
                                height: 8px;
                                border-radius: 50%;
                                background: ${module.status === 'ONLINE' || module.status === 'ACTIVE' || module.status === 'OPTIMIZED' ? '#10b981' : '#ef4444'};
                                margin-right: 5px;
                            "></span>
                            ${module.status}
                        </div>
                    </div>
                </div>
            `;
        }

        html += '</div>';
        this.container.innerHTML = html;
    }
}

// Expose to window
window.SentientCityDashboard = SentientCityDashboard;
