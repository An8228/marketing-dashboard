// src/api/analytics.ts

export type AnalyticsSummary = {
  total_campaigns: number;
  total_spend: number;
  total_revenue: number;
  roi: number;
};

export async function fetchAnalyticsSummary(): Promise<AnalyticsSummary> {
  return Promise.resolve({
    total_campaigns: 12,
    total_spend: 5400,
    total_revenue: 12000,
    roi: 50
  });
}

export type Recommendation = {
  id: string;
  title: string;
  description: string;
};

export async function fetchRecommendations(): Promise<Recommendation[]> {
  return Promise.resolve([
    {
      id: "rec-1",
      title: "Increase Email CTR",
      description: "Personalize subject lines for inactive users."
    },
    {
      id: "rec-2",
      title: "Improve Conversion Rate",
      description: "Retarget users who viewed pricing but didn’t convert."
    }
  ]);
}
