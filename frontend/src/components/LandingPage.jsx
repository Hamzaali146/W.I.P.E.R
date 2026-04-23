import Navbar from "@/components/landing/Navbar";
import HeroSection from "@/components/landing/HeroSection";
import AboutSection from "@/components/landing/AboutSection";
import FeaturesSection from "@/components/landing/FeaturesSection";
import HowItWorksSection from "@/components/landing/HowItWorksSection";
import ShowcaseSection from "@/components/landing/ShowcaseSection";
import TechStackSection from "@/components/landing/TechStackSection";
import TeamSection from "@/components/landing/TeamSection";
import FooterSection from "@/components/landing/FooterSection";

const LandingPage = () => {
  return (
    <div className="landing-theme min-h-screen bg-background font-display">
      <Navbar />
      <HeroSection />
      <AboutSection />
      <FeaturesSection />
      <HowItWorksSection />
      <ShowcaseSection />
      <TechStackSection />
      <TeamSection />
      <FooterSection />
    </div>
  );
};

export default LandingPage;
