import "./globals.css";
import { Toaster } from "@/components/ui/sonner"
import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "AgentLocate",
  description: "Look at me, I am the captain now. I will conquer the world and bla bla bla, will anyone really read this description?",
};

export default function RootLayout({children}: { children: React.ReactNode; }) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        <Toaster />
        {children}
      </body>
    </html>
  );
}
