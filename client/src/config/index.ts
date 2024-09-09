import { Metadata } from "next";

export const SITE_CONFIG: Metadata = {
    title: {
        // write a default title for astra a ai powered website builder suggest something unique and catchy don't use the same words of ai powered website builder give a unique name
        default: "Pitcher AI",
        template: `%s | Pitcher`
    },
    description: "Pitcher AI converts product reviews into impactful social media pitches using AI.",
    icons: {
        icon: [
            {
                url: "/icons/icon.png",
                href: "/icons/icon.png",
            }
        ]
    },
    openGraph: {
        title: "Pitcher AI - Turning Reviews into Winning Pitches.",
        description: "Pitcher AI converts product reviews into impactful social media pitches using AI.",
        images: [
            {
                url: "/assets/og-image.png",
            }
        ]
    },
    twitter: {
        card: "summary_large_image",
        creator: "@npm_shubham",
        title: "Pitcher AI - Turning Reviews into Winning Pitches",
        description: "Pitcher AI converts product reviews into impactful social media pitches using AI.",
        images: [
            {
                url: "/assets/og-image.png",
            }
        ]
    },
    metadataBase: new URL("https://pitcher-ai.vercel.app/"),
};
