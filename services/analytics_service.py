"""
Enhanced Analytics Service - Track user events with proper Umami integration
Supports: Umami, Plausible, PostHog
"""

import streamlit as st
import streamlit.components.v1 as components
from config.settings import (
    ANALYTICS_ENABLED,
    ANALYTICS_PROVIDER,
    UMAMI_CONFIG,
    PLAUSIBLE_CONFIG,
    POSTHOG_CONFIG
)

def inject_analytics_script():
    """Inject analytics tracking script in page header"""
    
    if not ANALYTICS_ENABLED:
        return
    
    if ANALYTICS_PROVIDER == "umami":
        # Umami Analytics - Proper initialization
        components.html(f"""
        <script async 
            data-website-id="{UMAMI_CONFIG['website_id']}" 
            src="{UMAMI_CONFIG['script_url']}"
            data-domains="{UMAMI_CONFIG.get('domain', 'localhost')}">
        </script>
        """, height=0)
    
    elif ANALYTICS_PROVIDER == "plausible":
        # Plausible Analytics
        components.html(f"""
        <script defer 
            data-domain="{PLAUSIBLE_CONFIG['domain']}" 
            src="{PLAUSIBLE_CONFIG['script_url']}">
        </script>
        """, height=0)
    
    elif ANALYTICS_PROVIDER == "posthog":
        # PostHog Analytics
        components.html(f"""
        <script>
            !function(t,e){{var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){{function g(t,e){{var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){{t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}}}(p=t.createElement("script")).type="text/javascript",p.async=!0,p.src=s.api_host+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){{var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e}},u.people.toString=function(){{return u.toString(1)+".people (stub)"}},o="capture identify alias people.set people.set_once set_config register register_once unregister opt_out_capturing has_opted_out_capturing opt_in_capturing reset isFeatureEnabled onFeatureFlags getFeatureFlag getFeatureFlagPayload reloadFeatureFlags group updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures getActiveMatchingSurveys getSurveys".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])}},e.__SV=1)}}(document,window.posthog||[]);
            posthog.init('{POSTHOG_CONFIG['api_key']}',{{api_host:'{POSTHOG_CONFIG['host']}'}})
        </script>
        """, height=0)


def track_event(event_name, properties=None):
    """
    Track custom event - UMAMI optimized
    
    Args:
        event_name: Name of the event
            - "generate_main_clicked" (Button 1 on landing page)
            - "generate_form_submitted" (Button 2 after form)
            - "pdf_downloaded"
        properties: Dict of additional properties
    """
    
    if not ANALYTICS_ENABLED:
        return
    
    properties = properties or {}
    
    if ANALYTICS_PROVIDER == "umami":
        # Umami custom event - Using umami.track()
        import json
        props_json = json.dumps(properties)
        
        components.html(f"""
        <script>
            // Wait for umami to be available
            (function() {{
                var attempts = 0;
                var maxAttempts = 10;
                
                function trackEvent() {{
                    if (typeof umami !== 'undefined') {{
                        umami.track('{event_name}', {props_json});
                        console.log('Umami tracked: {event_name}');
                    }} else if (attempts < maxAttempts) {{
                        attempts++;
                        setTimeout(trackEvent, 200);
                    }}
                }}
                
                trackEvent();
            }})();
        </script>
        """, height=0)
    
    elif ANALYTICS_PROVIDER == "plausible":
        # Plausible custom event
        props_str = ", ".join([f'"{k}": "{v}"' for k, v in properties.items()])
        components.html(f"""
        <script>
            if (typeof plausible !== 'undefined') {{
                plausible('{event_name}', {{props: {{{props_str}}}}});
            }}
        </script>
        """, height=0)
    
    elif ANALYTICS_PROVIDER == "posthog":
        # PostHog custom event
        props_str = ", ".join([f'"{k}": "{v}"' for k, v in properties.items()])
        components.html(f"""
        <script>
            if (typeof posthog !== 'undefined') {{
                posthog.capture('{event_name}', {{{props_str}}});
            }}
        </script>
        """, height=0)


def track_page_view(page_name):
    """Track page view"""
    track_event("page_view", {"page": page_name})


# Event name constants for consistency
EVENT_GENERATE_MAIN = "generate_main_clicked"  # Landing page button
EVENT_GENERATE_FORM = "generate_form_submitted"  # Form submit button
EVENT_PDF_DOWNLOADED = "pdf_downloaded"
EVENT_ADMIN_ACCESS = "admin_dashboard_accessed"